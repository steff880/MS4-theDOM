from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Course, Category
from .forms import CourseForm, ReviewForm


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
            if sortkey == 'category':
                sortkey = 'category__name'

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


@login_required
def course_detail(request, course_id):
    """
    A view to show individual course details
    """
    course = get_object_or_404(Course, pk=course_id)
    form = ReviewForm()

    context = {
        'course': course,
        'form': form,
    }

    return render(request, 'courses/course_detail.html', context)


@login_required
def add_review(request, course_id):
    """
    A view to allow the user to add a review to a course
    """

    course = get_object_or_404(Course, pk=course_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.course = course
                review.user = request.user
                review.save()
                messages.success(request, 'Your review was successful')
                return redirect(reverse('course_detail', args=[course.id]))
            else:
                messages.error(
                    request, 'Failed to add your review')
    context = {
        'form': form
    }

    return render(request, context)


@login_required
def add_course(request):
    """ Add a course to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Successfully added course!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(
                request,
                'Failed to add course. Please ensure the form is valid.')
    else:
        form = CourseForm()

    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_course(request, course_id):
    """ Edit course in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('course_detail', args=[course.id]))
        else:
            messages.error(
                request,
                'Failed to update course. Please ensure the form is valid.')
    form = CourseForm(instance=course)
    messages.info(request, f'You are editing {course.name}')

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)


@login_required
def delete_course(request, course_id):
    """ Delete a course from store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.success(request, 'Course deleted!')
    return redirect(reverse('courses'))
