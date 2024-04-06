
# pip install --upgrade loguru

from loguru import Logger, Level, LevelConfig, logger
import sys


# logger.add("debug.log", rotation="100 MB", compression="zip", level="DEBUG")
# logger.add(sys.stderr, level="DEBUG", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
# logger.add(sys.stderr, level="INFO", format="{time} {level} {message}", filter="my_module", serialize=True)
handler_id = logger.add("file_{time}.log", enqueue=False)
logger.remove(handler_id=handler_id)

level = logger.level("CUSTOM", no=5, icon="🐛", color="<blue>")
level.log("CUSTOM", "custom log")

logger.catch()
logger.debug()
logger.info()
logger.warning()
logger.exception()
logger.critical()