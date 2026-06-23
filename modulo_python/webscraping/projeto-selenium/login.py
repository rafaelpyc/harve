"""Funcoes de login no InfoJobs."""

import os

from dotenv import load_dotenv

from logger import logger
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL_LOGIN = "https://login.infojobs.com.br/Account/Login"

BUTTON_COOKIES_ACCEPT = '//*[@id="didomi-notice-agree-button"]'
BUTTON_CONTINUE = '//*[@id="loginForm"]/button'
FIELD_EMAIL = '//*[@id="Email"]'
FIELD_PASSWORD = '//*[@id="Password"]'


def carregar_credenciais() -> tuple[str, str]:
    # Credenciais ficam fora do codigo-fonte para evitar vazamento acidental em
    # commits, logs ou compartilhamento do projeto.
    load_dotenv(encoding="utf-8-sig")
    email = os.getenv("INFOJOBS_EMAIL")
    senha = os.getenv("INFOJOBS_SENHA")

    if not email or not senha:
        # Sem credenciais nao ha o que automatizar: registra o motivo no log e
        # encerra imediatamente, sem abrir navegador nem capturar snapshot.
        logger.error("Defina INFOJOBS_EMAIL e INFOJOBS_SENHA no arquivo .env.")
        raise SystemExit(1)

    return email, senha


def aceitar_cookies(driver: WebDriver) -> None:
    try:
        # O banner de cookies nem sempre aparece; por isso o timeout curto evita
        # atrasar o login quando o consentimento ja foi registrado.
        espera = WebDriverWait(driver, 5)
        botao = espera.until(
            EC.element_to_be_clickable((By.XPATH, BUTTON_COOKIES_ACCEPT))
        )
        botao.click()
    except TimeoutException:
        logger.warning("Botao de cookies nao apareceu.")
    except WebDriverException:
        raise RuntimeError("Falha ao tentar aceitar os cookies na tela de login.")


def verificar_login(driver: WebDriver) -> None:
    # Login correto redireciona para fora de login.infojobs.com.br; com senha
    # errada o formulario e reexibido e a URL permanece no dominio de login.
    # Checar a URL dispensa depender de um elemento especifico da pagina logada.
    espera = WebDriverWait(driver, 10)

    try:
        espera.until(
            lambda navegador: "login.infojobs.com.br" not in navegador.current_url
        )
    except TimeoutException:
        raise RuntimeError("Login falhou: verifique as credenciais no arquivo .env.")
    except WebDriverException:
        raise RuntimeError("Falha ao verificar o resultado do login.")


def fazer_login(driver: WebDriver, email: str, senha: str) -> None:
    # Esperas explicitas tornam o fluxo mais estavel que pausas fixas com sleep,
    # especialmente em paginas que carregam campos de forma assincrona.
    espera = WebDriverWait(driver, 10)

    try:
        driver.get(URL_LOGIN)
    except WebDriverException:
        raise RuntimeError("Nao foi possivel abrir a pagina de login do InfoJobs.")

    aceitar_cookies(driver)

    try:
        campo_email = espera.until(EC.element_to_be_clickable((By.XPATH, FIELD_EMAIL)))
        campo_email.send_keys(email)
        driver.find_element(By.XPATH, BUTTON_CONTINUE).click()
    except TimeoutException:
        raise RuntimeError("Campo de email nao ficou clicavel na tela de login.")
    except WebDriverException:
        raise RuntimeError("Falha ao preencher ou enviar o email no login.")

    try:
        campo_senha = espera.until(
            EC.element_to_be_clickable((By.XPATH, FIELD_PASSWORD))
        )
        campo_senha.send_keys(senha)
        driver.find_element(By.XPATH, BUTTON_CONTINUE).click()
    except TimeoutException:
        raise RuntimeError("Campo de senha nao ficou clicavel na tela de login.")
    except WebDriverException:
        raise RuntimeError("Falha ao preencher ou enviar a senha no login.")

    verificar_login(driver)
