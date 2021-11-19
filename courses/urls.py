from django.urls import path
from . import views

urlpatterns = [
   path('', views.all_courses, name='courses'),
   path('<int:course_id>/', views.course_detail, name='course_detail'),
   path('add_review/<int:course_id>/', views.add_review, name='add_review'),
   path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
   path('add/', views.add_course, name='add_course'),
   path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
   path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
]
