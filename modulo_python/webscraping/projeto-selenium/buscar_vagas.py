"""Busca, raspagem e salvamento de vagas."""

import pandas as pd

from logger import BASE_DIR, logger
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Seletores ancorados em atributos estaveis (name, id e classes js_*/jsBtn*,
# que o proprio JavaScript do site usa) em vez de caminhos posicionais do
# DevTools, que quebram a cada mudanca de layout.
FIELD_DESCRICAO = '//input[@name="Palabra"]'
BUTTON_ACHAR_VAGAS = '//a[contains(@class, "jsBtnSearch")]'
BUTTON_FECHAR_POPUP = '//*[@id="divBenefitsModal"]/div/div/span'

CARD_VAGA = '//div[contains(@class, "js_vacancyLoad")]'
TITULO_VAGA = './/h2[contains(@class, "js_vacancyTitle")]'
EMPRESA_VAGA = './/a[contains(@href, "empresa-")]'
# A localizacao e a primeira linha "text-medium" do card; a classe de
# tipografia e mais estavel que utilitarias de espacamento (mb-4/mb-8).
LOCAL_VAGA = './/div[contains(@class, "text-medium")]'


def fechar_popup(driver: WebDriver) -> None:
    try:
        # O pop-up de beneficios pode bloquear o campo de busca; fechar quando
        # ele existe deixa a proxima acao previsivel.
        espera = WebDriverWait(driver, 5, poll_frequency=0.2)
        botao_fechar = espera.until(
            EC.element_to_be_clickable((By.XPATH, BUTTON_FECHAR_POPUP))
        )
        botao_fechar.click()
    except TimeoutException:
        logger.warning("Pop-up nao apareceu.")
    except WebDriverException:
        raise RuntimeError("Falha ao tentar fechar o pop-up de beneficios.")


def buscar_vagas(driver: WebDriver, descricao: str) -> None:
    espera = WebDriverWait(driver, 10)

    fechar_popup(driver)

    try:
        campo_descricao = espera.until(
            EC.element_to_be_clickable((By.XPATH, FIELD_DESCRICAO))
        )
        campo_descricao.send_keys(descricao)
    except TimeoutException:
        raise RuntimeError("Campo de descricao da vaga nao ficou clicavel.")
    except WebDriverException:
        raise RuntimeError("Falha ao preencher a descricao da vaga.")

    try:
        driver.find_element(By.XPATH, BUTTON_ACHAR_VAGAS).click()
    except WebDriverException:
        raise RuntimeError("Falha ao clicar no botao de buscar vagas.")


def extrair_dados_card(card) -> dict[str, str]:
    try:
        # Estes campos sao considerados obrigatorios para a vaga ser util no CSV
        # e para permitir a etapa posterior de candidatura.
        titulo = card.find_element(By.XPATH, TITULO_VAGA).text
        local = card.find_element(By.XPATH, LOCAL_VAGA).text
        link = card.get_attribute("data-href")
    except NoSuchElementException:
        raise RuntimeError("Card de vaga sem titulo ou local obrigatorio.")
    except StaleElementReferenceException:
        raise RuntimeError("Card de vaga ficou obsoleto durante a leitura.")
    except WebDriverException:
        raise RuntimeError("Falha ao ler os dados obrigatorios do card.")

    if link and link.startswith("/"):
        # O InfoJobs pode retornar URLs relativas no atributo data-href.
        link = "https://www.infojobs.com.br" + link

    try:
        # Empresa e opcional porque alguns cards patrocinados ou incompletos nao
        # exibem esse campo de forma consistente.
        empresa = card.find_element(By.XPATH, EMPRESA_VAGA).text
    except NoSuchElementException:
        empresa = ""
    except StaleElementReferenceException:
        raise RuntimeError("Card de vaga ficou obsoleto ao ler a empresa.")
    except WebDriverException:
        raise RuntimeError("Falha ao ler a empresa do card de vaga.")

    return {
        "titulo": titulo,
        "empresa": empresa,
        "local": local,
        "link": link,
    }


def carregar_novos_cards(driver: WebDriver, cards) -> bool:
    if not cards:
        logger.warning("Nenhum card encontrado para continuar o scroll.")
        return False

    try:
        # A pagina usa carregamento incremental; rolar ate o fim dispara a busca
        # por novos cards antes da proxima rodada de raspagem.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except WebDriverException:
        raise RuntimeError("Falha ao rolar a pagina de vagas.")

    try:
        espera = WebDriverWait(driver, 10)
        espera.until(
            lambda navegador: (
                len(navegador.find_elements(By.XPATH, CARD_VAGA)) > len(cards)
            )
        )
    except TimeoutException:
        logger.warning("Nenhum card novo foi carregado apos o scroll.")
        return False
    except WebDriverException:
        raise RuntimeError("Falha ao carregar novos cards de vaga.")

    return True


def raspar_vagas(driver: WebDriver, max_vagas: int = 50) -> list[dict[str, str]]:
    espera = WebDriverWait(driver, 10)

    try:
        espera.until(EC.presence_of_all_elements_located((By.XPATH, CARD_VAGA)))

        vagas = []
        # Conta os cards ja processados separadamente de len(vagas), pois um
        # card invalido e pulado sem gerar vaga e nao pode ser lido de novo.
        processados = 0

        while len(vagas) < max_vagas:
            cards = driver.find_elements(By.XPATH, CARD_VAGA)

            # Reprocessar apenas os cards novos evita duplicidades apos cada
            # scroll e reduz chamadas desnecessarias ao WebDriver.
            for card in cards[processados:]:
                processados += 1

                try:
                    vaga = extrair_dados_card(card)
                except RuntimeError as erro:
                    # Um card incompleto (ex.: patrocinado) nao deve derrubar a
                    # raspagem inteira nem descartar as vagas ja coletadas.
                    logger.warning("Card {} ignorado: {}", processados, erro)
                    continue

                vagas.append(vaga)

                if len(vagas) >= max_vagas:
                    return vagas

            if not carregar_novos_cards(driver, cards):
                break

        return vagas
    except TimeoutException:
        raise RuntimeError("Nenhum card de vaga apareceu na pagina de resultados.")
    except WebDriverException:
        raise RuntimeError("Falha ao raspar os cards de vaga.")


def salvar_vagas(vagas: list[dict[str, str]]) -> None:
    arquivo = BASE_DIR / "dados" / "vagas_selenium.csv"
    arquivo.parent.mkdir(exist_ok=True)

    # utf-8-sig melhora a compatibilidade do CSV com Excel em ambientes Windows.
    df = pd.DataFrame(vagas)
    df.to_csv(arquivo, index=False, encoding="utf-8-sig")
    logger.info("Arquivo salvo em: {}", arquivo)
