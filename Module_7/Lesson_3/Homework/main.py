import logging.config

from logging_config import config

logging.config.dictConfig(config)


def get_logger(name: str | None = None) -> logging.Logger:
    if name is None:
        return logging.getLogger()
    return logging.getLogger(name)


root, sub_1, sub_2, sub_sub_1 = (
    get_logger(),
    get_logger("sub_1"),
    get_logger("sub_2"),
    get_logger("sub_2.sub_sub_1"),
)

all_loggers = (root, sub_1, sub_2, sub_sub_1)

for logger in all_loggers:
    logger.info(logger.parent)
