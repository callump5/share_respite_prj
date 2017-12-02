# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Donation(models.Model):
    stripe_id = models.CharField(max_length=40, default='')
    user = models.ForeignKey('auth.User', related_name='donations')
    amount = models.FloatField(default=0.00)