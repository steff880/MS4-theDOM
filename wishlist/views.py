from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import WishList


@login_required
def wishlist(request):
    """
    A view to render the user's wishlist
    """
    wishlist = None
    try:
        wishlist = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)
