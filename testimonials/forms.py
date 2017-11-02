from django import forms
from .models import TestimonialPost
from django.contrib.auth.models import User

class TestimonialPostForm(forms.ModelForm):

    class Meta:
        model = TestimonialPost
        fields = ('author', 'title', 'content')

