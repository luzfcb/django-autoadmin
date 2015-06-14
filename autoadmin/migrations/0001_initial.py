# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoAdminSingleton',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, null=True, verbose_name='Password', blank=True)),
                ('password_hash', models.CharField(max_length=128, null=True, verbose_name='Password hash', blank=True)),
                ('account', models.ForeignKey(verbose_name='Account', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Autoadmin properties',
                'verbose_name_plural': 'Autoadmin properties',
            },
            bases=(models.Model,),
        ),
    ]
