from __future__ import unicode_literals

from django.conf import settings

EMAIL = getattr(settings, 'AUTOADMIN_EMAIL', 'autoadmin@example.com')
PASSWORD = getattr(settings, 'AUTOADMIN_PASSWORD', None)
USERNAME = getattr(settings, 'AUTOADMIN_USERNAME', 'admin')
