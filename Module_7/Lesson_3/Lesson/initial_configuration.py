import logging.config

from logging_config import dict_config

logging.config.dictConfig(dict_config)

# module_logger = logging.getLogger("module_logger")
# module_logger.propagate = False
#
# formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(message)s")
#
# file_handler = logging.FileHandler("logfile.log", mode="a")
# file_handler.setFormatter(formatter)
# module_logger.addHandler(file_handler)
#
# console_handlers = logging.StreamHandler()
# console_handlers.setFormatter(formatter)
# module_logger.addHandler(console_handlers)

submodule_logger = logging.getLogger("module_logger.submodule_logger")
submodule_logger.setLevel(logging.DEBUG)


def main():
    submodule_logger.debug("Hi there!")


if __name__ == "__main__":
    main()
