"""Exemplo de fluxo para juntar as funcoes da aula."""

import argparse
import sys
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from buscar_vagas import buscar_vagas, raspar_vagas, salvar_vagas
from candidatar import candidatar
from logger import BASE_DIR, logger
from login import carregar_credenciais, fazer_login

SNAPSHOT_DIR = BASE_DIR / "logs" / "snapshots"


def iniciar_navegador() -> webdriver.Chrome:
    try:
        # Mantem a criacao do WebDriver isolada para facilitar ajustes futuros,
        # como modo headless, perfil dedicado ou opcoes especificas do Chrome.
        return webdriver.Chrome()
    except WebDriverException:
        raise RuntimeError("Nao foi possivel iniciar o Chrome WebDriver.")


def capturar_snapshot(driver: webdriver.Chrome) -> Path | None:
    if not driver:
        return None

    # O snapshot ajuda a diagnosticar falhas dependentes do estado visual da pagina,
    # muito comuns em automacoes Selenium.
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    arquivo = SNAPSHOT_DIR / f"erro_{datetime.now():%Y%m%d_%H%M%S}.png"

    try:
        driver.save_screenshot(str(arquivo))
    except WebDriverException:
        logger.warning("Nao foi possivel capturar snapshot do navegador.")
        return None

    return arquivo


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Automacao de busca e candidatura de vagas no InfoJobs."
    )
    parser.add_argument(
        "--busca",
        default="python",
        help="termo pesquisado no campo de vagas (padrao: %(default)s)",
    )
    parser.add_argument(
        "--vaga",
        type=int,
        default=None,
        help=(
            "indice do card para candidatura; sem este argumento, "
            "nenhuma candidatura e feita"
        ),
    )
    parser.add_argument(
        "--pausar-no-erro",
        action="store_true",
        help="mantem o navegador aberto para inspecao quando ocorre uma falha",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Credenciais sao validadas antes de qualquer navegador ser aberto: se o
    # .env estiver incompleto, o programa apenas loga o motivo e encerra.
    email, senha = carregar_credenciais()

    driver = None

    try:
        driver = iniciar_navegador()

        # Fluxo principal: autentica, pesquisa, extrai os cards e tenta uma
        # candidatura controlada pelos argumentos de linha de comando.
        fazer_login(driver, email, senha)
        buscar_vagas(driver, descricao=args.busca)

        vagas = raspar_vagas(driver, max_vagas=50)
        salvar_vagas(vagas)

        # Candidatura e opt-in: so acontece quando o usuario passa --vaga,
        # evitando inscricoes acidentais em execucoes de teste ou raspagem.
        if args.vaga is not None:
            candidatar(driver, vagas, indice_card=args.vaga)
        else:
            logger.info("Sem --vaga: etapa de candidatura pulada.")
    except RuntimeError as erro:
        snapshot = capturar_snapshot(driver)
        logger.exception("Falha na automacao: {}", erro)

        if snapshot:
            logger.error("Snapshot do erro salvo em: {}", snapshot)

        # A pausa e opcional e restrita a execucoes interativas; sem o isatty,
        # um input() com stdin fechado levantaria EOFError e mascararia o erro.
        if args.pausar_no_erro and sys.stdin.isatty():
            input("Inspecione o navegador e pressione Enter para fechar...")

        raise SystemExit(1) from erro
    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()
