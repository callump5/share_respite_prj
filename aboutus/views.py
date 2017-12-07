# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import StaffDetails, WhatsOn

# Create your views here.

def staff_list(request):
    staffs = StaffDetails.objects.all()
    return render(request, "aboutus/staff.html", {'staffs': staffs})

def whats_on(request):
    activities = WhatsOn.objects.all()
    return render(request, "aboutus/whats-on.html", {'activities': activities})

def contact(request):
    return render(request, 'aboutus/contact_us.html')