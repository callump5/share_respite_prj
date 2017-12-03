# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from .models import Donation

class DonationForm(forms.ModelForm):
    amount = forms.CharField(label='Donation, e.g 1.50 = £1.50',)


    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar',
        'Apr', 'May', 'June',
        'July', 'Aug', 'Sept',
        'Oct', 'Nov', 'Dec'
    ]

    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)'
                          )
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)

    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Donation
        fields = ['amount', 'stripe_id']