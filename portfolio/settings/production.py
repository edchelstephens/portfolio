import os

from portfolio.settings.base import *  # noqa

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, "static/")  # noqa

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
