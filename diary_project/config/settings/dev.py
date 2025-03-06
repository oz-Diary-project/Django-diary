from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "drf_yasg",  # 또는 "drf_spectacular"
]
