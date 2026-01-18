from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<light-cyan>{function}</light-cyan>:<light-blue>{line}</light-blue> → <level>{message}</level>",
    level="INFO"
)

# You will use: logger.info("Hello from RPi!")