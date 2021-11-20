from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from courses.models import Course
from .models import WishList


# Ref:
# https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/wishlist/views.py
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


@login_required
def add_to_wishlist(request, course_id):
    """
    Add a course to the
    wishlist for the logged in user
    """
    course = get_object_or_404(Course, pk=course_id)

    # Create a wishlist for the user if they don't have one
    wishlist, _ = WishList.objects.get_or_create(user=request.user)
    # Add course to the wishlist
    wishlist.courses.add(course)
    messages.info(request, "A new course was added to your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, course_id):
    """
    Add a course from the store to the
    wishlist for the logged in user
    """
    wishlist = WishList.objects.get(user=request.user)
    course = get_object_or_404(Course, pk=course_id)

    # Remove course from the wishlist
    wishlist.courses.remove(course)
    messages.info(request, "A course was removed from your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))
