# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import StaffDetails, WhatsOn

# Register your models here.



admin.site.register(StaffDetails)
admin.site.register(WhatsOn)