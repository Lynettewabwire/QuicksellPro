# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalApp', '0007_auto_20150924_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
    ]
