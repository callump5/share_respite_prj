# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Subject(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


    def __unicode__(self):
        return self.subject

class Thread(models.Model):
    thread = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    def __unicode__(self):
        return self.thread


class Comment(models.Model):
    thread = models.ForeignKey(Thread, related_name='comments')
    user = models.ForeignKey('auth.User', related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.user.get_full_name()




