from django.contrib import admin
from .models import Course, Category, CourseReview


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image', 'video',)

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CourseReview)
