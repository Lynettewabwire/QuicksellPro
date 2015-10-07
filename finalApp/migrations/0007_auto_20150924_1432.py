# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalApp', '0006_auto_20150924_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
