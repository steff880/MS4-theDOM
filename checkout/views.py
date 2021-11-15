from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag at the moment')
        return redirect(reverse('courses'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JadgmGOeR1XPIDzaDHw3ScUJlAWtpvlLaGNoIjq9W2ziOSnleedQ87IlszT7Qj2kdwT4mULecSdVVx40qEt1Ppi00VqSqCrUc',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
