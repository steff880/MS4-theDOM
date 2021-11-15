from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

import stripe
from bag.contexts import bag_contents
from courses.models import Course
from .models import OrderLineItem
from .forms import OrderForm


def checkout(request):
    """
    A view that handles the checkout process
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    course = Course.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        course=course,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Course.DoesNotExist:
                    messages.error(request, (
                        "One of the courses doesn't seem to exist,"
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save-info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, 'There is nothing in your bag at the moment')
            return redirect(reverse('courses'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
