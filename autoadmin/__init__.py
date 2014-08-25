from django.core.exceptions import ImproperlyConfigured

try:
    from .handlers import autoadmin_create, autoadmin_account_passwd_change  # NOQA
except ImproperlyConfigured:
    # Ignore this exception during setup.py
    pass

__author__ = 'Roberto Rosario'
__build__ = 0x000500
__copyright__ = 'Copyright 2014 Roberto Rosario'
__license__ = 'MIT'
__title__ = 'django-autoadmin'
__version__ = '0.5.0'
