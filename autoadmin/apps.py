from __future__ import unicode_literals

from django import apps
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from .handlers import auto_admin_account_password_change


class AutoAdminAppConfig(apps.AppConfig):
    name = 'autoadmin'
    verbose_name = _('Autoadmin')

    def ready(self):
        post_save.connect(
            auto_admin_account_password_change,
            dispatch_uid='auto_admin_account_password_change',
            sender=settings.AUTH_USER_MODEL
        )
