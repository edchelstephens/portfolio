from portfolio.settings.base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1"]

DEVELOPMENT_APPS = ["django_extensions", "django_browser_reload"]
DEVELOPMENT_MIDDLEWARES = ["django_browser_reload.middleware.BrowserReloadMiddleware"]

INSTALLED_APPS += DEVELOPMENT_APPS  # noqa
MIDDLEWARE += DEVELOPMENT_MIDDLEWARES  # noqa
