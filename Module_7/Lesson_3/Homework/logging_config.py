config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "formatter": {
            "format": "%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s: %(lineno)d"
        }
    },
    "handlers": {
        "handler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "formatter",
        },
        "root_logger": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "formatter",
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "formatter",
            "filename": "homelogs.log",
            "mode": "a",
        },
    },
    "loggers": {
        "sub_1": {
            "level": "INFO",
            "handlers": ["handler", "file_handler"],
            "propagate": True,
        },
        "sub_2": {
            "propagate": False,
            "handlers": ["file_handler"],
        },
        "sub_2.sub_sub_1": {
            "handlers": ["handler"],
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["root_logger"],
    },
}
