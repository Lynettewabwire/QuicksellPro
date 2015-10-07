# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalApp', '0009_auto_20150924_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='image',
            field=models.FileField(upload_to=b'images/', blank=True),
        ),
    ]
