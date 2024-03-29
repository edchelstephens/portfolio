from .base import *  # noqa

DEBUG = False

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "django.log",
        },
        "contact": {
            "class": "logging.FileHandler",
            "filename": "contact.log",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "contact": {
            "level": "DEBUG",
            "handlers": ["contact"],
        },
    },
}
