from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Course, Category


def all_courses(request):
    """
    A view to show all courses,
    inluding sorting and search queries
    """

    courses = Course.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                courses = courses.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            courses = courses.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            courses = courses.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, 'You did not enter any search criteria!')
                return redirect(reverse('courses'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            courses = courses.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'courses': courses,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
