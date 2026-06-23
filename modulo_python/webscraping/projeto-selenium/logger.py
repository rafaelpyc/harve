"""Configuracao central de logs da automacao Selenium."""

from pathlib import Path
import sys

from loguru import logger

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"

# Remove o handler padrao do Loguru para manter um formato unico no terminal e
# no arquivo de log.
logger.remove()
logger.add(
    sys.stderr,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
)
logger.add(
    LOG_FILE,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    encoding="utf-8",
    # Rotacao e retencao evitam crescimento indefinido do log durante testes.
    rotation="1 MB",
    retention="7 days",
)
