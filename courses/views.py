from django.shortcuts import render
from .models import Course


def all_courses(request):
    """
    A view to show all courses,
    inluding sorting and search queries
    """

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)
