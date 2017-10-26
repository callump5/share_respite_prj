# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class TestimonialPost(models.Model):
    author_key = models.ForeignKey('auth.User')
    author = models.CharField(max_length=200, default='Anonymous')
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title
