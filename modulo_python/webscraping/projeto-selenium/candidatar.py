"""Candidatura em uma vaga do InfoJobs."""

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logger import logger

# Classe js_* usada pelo proprio JavaScript do site; mais estavel que
# caminhos posicionais copiados do DevTools.
BUTTON_CANDIDATAR = '//a[contains(@class, "js_btApplyVacancy")]'


def selecionar_vaga(
    vagas: list[dict[str, str]],
    indice_card: int,
) -> dict[str, str]:
    # O indice permite controlar manualmente qual card sera usado, evitando
    # candidaturas acidentais em massa. Indices negativos sao rejeitados para
    # nao selecionar, por engano, um card contado a partir do fim da lista.
    if not 0 <= indice_card < len(vagas):
        raise RuntimeError(
            f"Indice {indice_card} invalido: ha {len(vagas)} vagas "
            f"(use de 0 a {len(vagas) - 1})."
        )

    vaga = vagas[indice_card]

    if not vaga.get("link"):
        raise RuntimeError(f"A vaga no indice {indice_card} nao possui link.")

    return vaga


def abrir_vaga(driver: WebDriver, link: str) -> None:
    try:
        driver.get(link)
    except WebDriverException:
        raise RuntimeError("Nao foi possivel abrir a pagina da vaga.")


def clicar_candidatar(driver: WebDriver) -> None:
    espera = WebDriverWait(driver, 10)

    try:
        botao = espera.until(EC.element_to_be_clickable((By.XPATH, BUTTON_CANDIDATAR)))
        botao.click()
    except TimeoutException:
        raise RuntimeError(
            "Botao de candidatura nao ficou clicavel; a candidatura pode ja "
            "ter sido realizada ou o layout da pagina mudou."
        )
    except WebDriverException:
        raise RuntimeError("Falha ao clicar no botao de candidatura.")


def voltar_apos_candidatura(driver: WebDriver, url_vaga: str) -> None:
    # O clique em CANDIDATAR-ME carrega outra pagina (etapa pos-candidatura do
    # InfoJobs). Esperar a URL mudar confirma que o clique surtiu efeito, e o
    # driver.back() retorna a pagina anterior para o navegador terminar o
    # fluxo em um estado conhecido.
    espera = WebDriverWait(driver, 10)

    try:
        espera.until(lambda navegador: navegador.current_url != url_vaga)
    except TimeoutException:
        raise RuntimeError("Nenhuma pagina carregou apos o clique de candidatura.")
    except WebDriverException:
        raise RuntimeError("Falha ao aguardar a pagina pos-candidatura.")

    try:
        driver.back()
    except WebDriverException:
        raise RuntimeError("Falha ao voltar para a pagina da vaga.")


def candidatar(
    driver: WebDriver,
    vagas: list[dict[str, str]],
    indice_card: int = 0,
) -> None:
    # Mantem a sequencia de candidatura em passos pequenos para facilitar
    # manutencao quando o InfoJobs alterar layout ou regras do formulario.
    vaga = selecionar_vaga(vagas, indice_card)

    logger.info(
        "Iniciando candidatura para card {}: {}",
        indice_card,
        vaga["titulo"],
    )
    abrir_vaga(driver, vaga["link"])

    # A URL e capturada depois de abrir a vaga (e nao do link do card) porque
    # o site pode aplicar redirecionamentos ao carregar a pagina.
    url_vaga = driver.current_url
    clicar_candidatar(driver)
    voltar_apos_candidatura(driver, url_vaga)

    logger.info(
        "Candidatura enviada para card {}: {}",
        indice_card,
        vaga["titulo"],
    )
