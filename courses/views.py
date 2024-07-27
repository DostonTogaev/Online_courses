from django.shortcuts import render,get_object_or_404

from courses.models import Course
from teachers.models import Teacher

# Create your views here.

def courses(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)

def courses_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,

    }
    return render(request, 'courses/courses_detail.html', context)
