import logging

logger_utils = logging.getLogger("logger_utils")

root_logger = logging.getLogger()
main_logger = logging.getLogger("main")
main_logger.setLevel(logging.INFO)
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)


def main():
    print(root_logger)
    print(main_logger, main_logger.parent)
    print(utils_logger, utils_logger.parent)


if __name__ == "__main__":
    main()
