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

@login_required(login_url='/login/')
def new_subject(request):

    if request.method == 'POST':

        subject_form = SubjectForm(request.POST)

        if subject_form.is_valid():
            subject = subject_form.save(False)
            subject.created_at = timezone.now()
            subject.save()

        messages.success(request, 'You successfully created a new subject!')

        return redirect(reverse('forum'))

    else:

        subject_form = SubjectForm()

    return render(request, 'forum/forms/subject_form.html', {'form': subject_form})


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
def delete_subject(request, subject_id):
    post = get_object_or_404(Subject, pk=subject_id)

    post.delete()
    messages.success(request, 'You successfully deleted a forum subject')
    return redirect(reverse('profile'))

@login_required(login_url='/login/')
def edit_subject(request, subject_id):
    post = get_object_or_404(Subject, pk=subject_id)


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

    messages.success(request, 'You successfully edited a forum subject')

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
    subject = get_object_or_404(Subject, pk=subject_id)

    thread.save(False)
    thread.views += 1
    thread.save()

    return render(request, 'forum/thread_post.html', {'thread': thread, 'subject':subject})

@login_required(login_url='/login/')
def new_comment(request, subject_id, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(False)
            comment.thread = thread
            comment.user = request.user
            comment.save()

            messages.success(request, 'You successfully created a comment!')

            return redirect('view_thread', subject_id, thread_id)

    else:
        comment_form = CommentForm()

    args = {
        'form': comment_form,
        'thread': thread
    }

    args.update(csrf(request))

    return render(request, 'forum/forms/comment_form.html', args)







