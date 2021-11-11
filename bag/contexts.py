from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course


def bag_contents(request):
    """
    Show items in the shopping bag,
    calculate the discount (if any),
    provide the total and if shopper has to
    spend more to get the discount.
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        course = get_object_or_404(Course, pk=item_id)
        total += quantity + course.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
        })

    if total < settings.DISCOUNT_THRESHOLD:
        discount = 0
        discount_delta = settings.DISCOUNT_THRESHOLD - total
    else:
        discount = total * Decimal(settings.DISCOUNT_PERSENTAGE / 100)
        discount_delta = 0

    grand_total = total - discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
