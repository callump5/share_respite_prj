# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import TestimonialPost
from .forms import TestimonialPostForm
from django.utils import timezone

# Create your views here.

def testimonial_list(request):
    posts = TestimonialPost.objects.all()
    return render(request, 'testimonials/testimonial_list.html', {'posts': posts})

@login_required(login_url='/login/')
def new_testimonial(request):
    if request.method == 'POST':
        form = TestimonialPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_key = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(testimonial_list)
    else:
        form = TestimonialPostForm()
    return render(request, 'testimonials/testimonial_form.html', {'form': form})
