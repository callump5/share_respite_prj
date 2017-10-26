from django import forms
from .models import TestimonialPost

class TestimonialPostForm(forms.ModelForm):
    class Meta:
        model = TestimonialPost
        fields = ('author', 'content')