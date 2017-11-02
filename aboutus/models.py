# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StaffDetails(models.Model):
    staff_key = models.ForeignKey('auth.User')
    image = models.ImageField(upload_to='staff_images', blank=True, null=True)
    bio = models.TextField()
    role = models.CharField(max_length=100, blank=True, null=True)
    interests = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.staff_key.get_full_name()

class WhatsOn(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()

    def __unicode__(self):
        return self.title