from __future__ import unicode_literals

import logging

from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_syncdb
from django.dispatch import receiver

import autoadmin
from .models import AutoAdminSingleton
from .settings import EMAIL, PASSWORD, USERNAME, ENABLE

logger = logging.getLogger(__name__)


@receiver(post_syncdb, dispatch_uid='autoadmin_create')
def autoadmin_create(sender, **kwargs):
    """
    Create our own admin super user automatically whenever the post migrate
    signal is triggered.
    """

    if kwargs['app'] == autoadmin.models:
        # Only create the auto admin once, on our own post syncdb signal
        AutoAdminSingleton.objects.get_or_create()

        if ENABLE:
            try:
                User.objects.get(username=USERNAME)
            except User.DoesNotExist:
                logger.info('Creating super admin user -- login: %s, password: %s' % (USERNAME, PASSWORD))
                assert User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
                admin = User.objects.get(username=USERNAME)

                # Store the auto admin password properties to display the first
                # login message
                autoadmin_properties, created = AutoAdminSingleton.objects.get_or_create()
                autoadmin_properties.account = admin
                autoadmin_properties.password = PASSWORD
                autoadmin_properties.password_hash = admin.password
                autoadmin_properties.save()
            else:
                logger.info('Super admin user already exists. -- login: %s' % USERNAME)


@receiver(post_save, dispatch_uid='autoadmin_account_passwd_change', sender=User)
def autoadmin_account_passwd_change(sender, instance, **kwargs):
    autoadmin_properties = AutoAdminSingleton.objects.get()
    if instance == autoadmin_properties.account and instance.password != autoadmin_properties.password_hash:
        # Only delete the auto admin properties if the password was changed
        autoadmin_properties.account = None
        autoadmin_properties.password = None
        autoadmin_properties.password_hash = None
        autoadmin_properties.save()
