from .settings import *

PROD_SECRET_KEY = 'django-insecure-clp&7kvoeya-e9mqwqb^0i0k5s%q0fpx3x2k6*xjd)_tfnx&%c'

SECRET_KEY = PROD_SECRET_KEY

DEBUG = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
