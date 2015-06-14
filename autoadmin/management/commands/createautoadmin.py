from __future__ import unicode_literals

import logging

from django.contrib.auth import get_user_model
from django.core import management
from django.core.management.base import BaseCommand, CommandError

from ...models import AutoAdminSingleton
from ...settings import EMAIL, PASSWORD, USERNAME

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Used to create a superuser with a secure and automatic password.'

    def handle(self, *args, **options):
        UserModel = get_user_model()

        # Get an usable password before creating the superuser
        if PASSWORD:
            try:
                # Let's try to see if it is a callable
                password = PASSWORD()
            except TypeError:
                password = PASSWORD
        else:
            password = get_user_model().objects.make_random_password()

        try:
            UserModel.objects.get(**{UserModel.USERNAME_FIELD: USERNAME})
        except UserModel.DoesNotExist:
            logger.info(
                'Creating superuser -- login: %s, email: %s, password: %s',
                USERNAME, EMAIL, password
            )
            management.call_command(
                'createsuperuser',
                **{
                    UserModel.USERNAME_FIELD: USERNAME,
                    'email': EMAIL,
                    'interactive': False
                }
            )

            account = UserModel.objects.get(
                **{
                    UserModel.USERNAME_FIELD: USERNAME
                }
            )
            account.set_password(raw_password=password)
            account.save()
            # Store the auto admin password properties to display the
            # first login message
            auto_admin_properties, created = AutoAdminSingleton.objects.get_or_create()
            auto_admin_properties.account = account
            auto_admin_properties.password = password
            auto_admin_properties.password_hash = account.password
            auto_admin_properties.save()
        else:
            raise CommandError('Superuser %s already exists.' % USERNAME)
            logger.error(
                'Super admin user already exists. -- login: %s', USERNAME
            )
