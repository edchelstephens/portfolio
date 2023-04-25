import os

from .base import *  # noqa
from .base import BASE_DIR, env

DEBUG = False


STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", os.path.join(BASE_DIR, "staticfiles/"))
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles/")

ROOT_URLCONF = "portfolio.urls"

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
