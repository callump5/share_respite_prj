# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib import messages
from donations.forms import DonationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.


def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=form.cleaned_data['amount'],
                    currency="GBP",
                    card=form.cleaned_data['stripe_id'],
                )

                if customer.paid:
                    donation_form = form.save(False)
                    donation_form.user = request.user
                    donation_form.save()

                    amount = donation_form.amount / 100
                    messages.success(request, "You donated £%s" % amount)
                    return redirect(reverse('profile'))
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

    else:
        form = DonationForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
    return render(request, 'donations/donation_form.html', args)

