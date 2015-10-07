# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finalApp', '0012_auto_20150925_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=50)),
                ('last_name', models.CharField(default=b'', max_length=50)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$')])),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(default=b'kampala', max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(default=b'', max_length=254)),
                ('password', models.CharField(default=b'', max_length=30)),
                ('confirm_password', models.CharField(default=b'', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
