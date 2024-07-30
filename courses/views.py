from django.shortcuts import render, get_object_or_404,redirect

from courses.models import Course
from courses.forms import CommentModelForm
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

def add_comment(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    form = CommentModelForm()
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = course
            comment.save()
            return redirect('courses_detail', course_id)
    context = {
        'form': form,
        'course': course,
    }

    return render(request, 'courses/courses_detail.html', context)