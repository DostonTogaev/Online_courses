from django.shortcuts import render, get_object_or_404, redirect

from teachers.models import Teacher


# Create your views here.
def teachers(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers': teachers
    }
    return render(request, 'teachers/teachers.html', context)

def teacher_details(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    context = {
        'teacher': teacher
    }
    return render(request, 'teachers/teacher_detail.html', context)
