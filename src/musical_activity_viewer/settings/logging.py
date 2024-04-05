import logging


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": 11,
            "propagate": False,
            "format": "\n".join(
                [
                    "👉 %(levelname)s: L%(lineno)d @ %(pathname)s",
                    "%(message)s",
                ],
            ),
        },
    },
}
