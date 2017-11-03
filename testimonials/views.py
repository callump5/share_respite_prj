# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from .models import TestimonialPost
from .forms import TestimonialPostForm
from django.utils import timezone


# Create your views here.

def testimonial_list(request):
    posts = TestimonialPost.objects.filter(published_date__lte=timezone.now()
		).order_by('-published_date')
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
            messages.success(request, 'Successfully created a new testimonial')
            return redirect('profile')
    else:
        form = TestimonialPostForm()
    return render(request, 'testimonials/testimonial_form.html', {'form': form})

@login_required(login_url='/login/')
def delete_testimonial(request, post_id):
    post = get_object_or_404(TestimonialPost, pk=post_id)

    if post.user_id == request.user.id:

        post.delete()
        return redirect(reverse('profile'))
    else:
        messages.error(request, "That post doesnt belong to you!")
        return redirect('profile')

@login_required(login_url='/login/')
def edit_testimonial(request, post_id):
    post = get_object_or_404(TestimonialPost, pk=post_id)

    if post.user_id == request.user.id:

        if request.method == "POST":
            form = TestimonialPostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()

                return redirect(reverse('profile'))
        else:
            form = TestimonialPostForm(instance=post)

        args = {
           'form': form,
        }

        args.update(csrf(request))

        return render(request, 'testimonials/testimonial_form.html', args)
    else:
        messages.error(request, "That post doesnt belong to you!")
        return redirect('profile')



