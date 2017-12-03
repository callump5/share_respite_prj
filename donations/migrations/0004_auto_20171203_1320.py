# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_auto_20171202_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
