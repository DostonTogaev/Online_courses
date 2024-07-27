from django.contrib import admin
from django.urls import path, include
from courses.views import courses, courses_detail
urlpatterns = [
    path('courses/', courses, name='courses'),
    path('course/<int:course_id>/', courses_detail, name='courses_detail'),

]