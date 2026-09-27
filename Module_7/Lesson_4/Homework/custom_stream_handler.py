import logging.config
import sys
from pprint import pprint


class CustomStreamHandler(logging.Handler):
    def __init__(self, stream=sys.stderr):
        super().__init__()
        self.stream = stream

    def emit(self, record: logging.LogRecord):
        pprint(record)
        message = self.format(record)
        print(message + "\n", file=self.stream)


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {"format": "%(levelname)s | %(name)s | %(message)s | %(very)s"}
    },
    "handlers": {
        "console": {
            "()": CustomStreamHandler,
            "level": "DEBUG",
            "formatter": "base",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "logfile.log",
            "mode": "a",
        },
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
            # "propagate": False,
        }
    },
    # "filters": {},
    # "root": {} # == "": {}
}

logging.config.dictConfig(dict_config)

module_logger = logging.getLogger("module_logger")

module_logger.debug("msg")  # , extra={"very": "much"})
