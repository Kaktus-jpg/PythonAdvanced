import logging
import time

import requests
from main import logger_utils  # noqa: F401

logger = logging.getLogger("logger_utils.http_utils")
logger.setLevel(logging.INFO)

GET_IP_URL = "https://api.ipify.org?format=json"


def get_ip_address() -> str:
    logger.debug("Start getting IP address")
    start = time.time()
    try:
        ip = requests.get(GET_IP_URL).json()["ip"]
    except Exception as exc:
        logger.exception(exc)
        raise
    logger.debug(f"Done requesting ip in {time.time() - start:.4f} seconds")
    logger.info(f"Ip address: {ip}")
    return ip
