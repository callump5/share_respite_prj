# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib import messages
from .forms import DonationForm
from .models import Donation
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.

@login_required(login_url='/login/')
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

def donations(request):
    return render(request, 'donations/donations.html')

def get_donations(request):

    data = Donation.objects.all()

    return JsonResponse(list(data))

