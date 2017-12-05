# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Donation(models.Model):
    user = models.ForeignKey('auth.User', related_name='donations')
    amount = models.DecimalField(decimal_places=2, max_digits=5, default=0.00)
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.amount