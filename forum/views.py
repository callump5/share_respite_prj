# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.shortcuts import render, get_object_or_404, redirect, reverse

from .forms import *

# Create your views here.

def forum(request):
    subjects = Subject.objects.all()
    return render(request, 'forum/forum.html', {'subjects': subjects})

def subject_details(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'forum/subject_threads.html', {'subject': subject})


@login_required(login_url='/login/')
def new_thread(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)

    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            thread = thread_form.save(False)
            thread.subject = subject
            thread.user = request.user
            thread.save()

            messages.success(request, 'You successfully created a new thread!')

            return redirect(reverse('profile'))

    else:
        thread_form = ThreadForm()

    args = {
        'form': thread_form,
        'subject': subject
    }

    args.update(csrf(request))

    return render(request, 'forum/forms/thread_form.html', args)

@login_required(login_url='/login/')
def delete_thread(request, subject_id, thread_id):
    post = get_object_or_404(Thread, pk=thread_id)

    if post.user_id == request.user.id:

        post.delete()
        return redirect(reverse('profile'))
    else:
        messages.error(request, "That post doesnt belong to you!")
        return redirect('profile')

@login_required(login_url='/login/')
def edit_thread(request, subject_id, thread_id):
    post = get_object_or_404(Thread, pk=thread_id)

    if post.user_id == request.user.id:

        if request.method == "POST":
            form = ThreadForm(request.POST, instance=post)
            if form.is_valid():
                form.save()

                return redirect(reverse('profile'))
        else:
            form = ThreadForm(instance=post)

        args = {
           'form': form,
        }

        args.update(csrf(request))

        return render(request, 'forum/forms/thread_form.html', args)
    else:
        messages.error(request, "That post doesnt belong to you!")
        return redirect('profile')


def view_thread(request, subject_id, thread_id):

    thread = get_object_or_404(Thread, pk=thread_id)

    return render(request, 'forum/thread_post.html', {'thread': thread})