# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 15:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='staff_images')),
                ('bio', models.TextField()),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('interests', models.CharField(blank=True, max_length=100, null=True)),
                ('staff_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
