# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('finalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='email',
            field=models.EmailField(max_length=254, unique=True, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254, unique=True, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254, unique=True, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
