from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel


class AutoAdminSingleton(SingletonModel):
    account = models.ForeignKey(User, blank=True, null=True,
                                verbose_name=_('Account'))
    password = models.CharField(blank=True, max_length=128, null=True,
                                verbose_name=_('Password'))
    password_hash = models.CharField(blank=True, max_length=128, null=True,
                                     verbose_name=_('Password hash'))

    class Meta:
        verbose_name = verbose_name_plural = _('Autoadmin properties')
