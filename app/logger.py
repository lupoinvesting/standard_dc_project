import logging
from .config import config

logger = logging.getLogger("DC_BOT")
logger.setLevel(config.general.log_level)
formatter = logging.Formatter(
    "%(name)-9s - %(levelname)-8s - %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
