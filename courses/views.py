from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Course


def all_courses(request):
    """
    A view to show all courses,
    inluding sorting and search queries
    """

    courses = Course.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, 'You did not enter any search criteria!')
                return redirect(reverse('courses'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            courses = courses.filter(queries)
    context = {
        'courses': courses,
        'search_term': query,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """
    A view to show individual course details
    """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)
