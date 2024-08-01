from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator

from teachers.models import Teacher


# Create your views here.

class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        search_query = request.GET.get('search', '')
        paginator = Paginator(teachers, 3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            'teachers': teachers,
            'search_query': search_query,
            'page_obj': page_obj,
        }
        return render(request, 'teachers/teachers.html', context)

class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, pk=teacher_id)

        context = {
            'teacher': teacher
        }
        return render(request, 'teachers/teacher_detail.html', context)


