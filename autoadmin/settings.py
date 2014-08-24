from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User

EMAIL = getattr(settings, 'AUTOADMIN_EMAIL', 'autoadmin@autoadmin.com')
PASSWORD = getattr(settings, 'AUTOADMIN_PASSWORD',
                   User.objects.make_random_password())
USERNAME = getattr(settings, 'AUTOADMIN_USERNAME', 'admin')
ENABLE = getattr(settings, 'AUTOADMIN_ENABLE', True)
