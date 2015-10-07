# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalApp', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='description',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2),
        ),
    ]
