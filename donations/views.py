# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Sum, Count
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

            charge = int(float(form.cleaned_data['amount']) * 100)

            try:
                customer = stripe.Charge.create(
                    amount= charge,
                    currency="GBP",
                    card=form.cleaned_data['stripe_id'],
                )

                chargeData = float(charge) / 100

                if customer.paid:
                    donation_form = form.save(False)
                    donation_form.user = request.user
                    donation_form.amount = chargeData
                    donation_form.save()

                    messages.success(request, "Thank you for donating £%s!" % chargeData)
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

def donation_graphs(request):

    donations = Donation.objects.all()

    total = 0
    for donation in donations:
        total += donation.amount

    return render(request, 'donations/donations.html', {'total': total})

