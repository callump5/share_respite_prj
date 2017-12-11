from django import forms
from .models import *

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject', ]
class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['thread', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]

