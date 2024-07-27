from django.contrib import admin
from django.urls import path, include
from teachers.views import teachers, teacher_details
urlpatterns = [
    path('teachers/', teachers, name='teachers'),
    path('teacher_details/<int:teacher_id>/', teacher_details, name='teacher_details'),

]