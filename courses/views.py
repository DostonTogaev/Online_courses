from datetime import datetime
from django.views import View

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from courses.models import Course, Category, Comment
from courses.forms import CommentModelForm
from django.db.models import Q
from teachers.models import Teacher
from django.db.models import Max


# Create your views here.

class CourseListView(View):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        categories = Category.objects.all()
        search_query = request.GET.get('search', '')
        count = categories.count()
        if search_query:
            try:
                price_query = float(search_query)
                courses = Course.objects.filter(
                    Q(title__icontains=search_query) | Q(price=price_query)
                )
            except ValueError:
                courses = Course.objects.filter(
                    Q(title__icontains=search_query)
                )
        paginator = Paginator(courses, 3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            'courses': courses,
            'categories': categories,
            'count': count,
            'page_obj': page_obj,
        }
        return render(request, 'courses/courses.html', context)




class CourseDetailView(View):
    def get(self, request, course_id,*args, **kwargs):
        course = get_object_or_404(Course, pk=course_id)
        teacher = Teacher.objects.all()
        comments = Comment.objects.filter(course=course_id)

        count = course.comments.count()

        context = {
            'course': course,
            'comments': comments,
            'count': count,
            'teacher': teacher,


        }
        return render(request, 'courses/courses_detail.html', context)



class AddCommentView(View):
    def get(self, request, course_id, *args, **kwargs):
        course = get_object_or_404(Course, pk=course_id)
        form = CommentModelForm()
        return render(request, 'courses/courses_detail.html', {'course': course, 'comment_form': form})

    def post(self, request, course_id, *args, **kwargs):
        course = get_object_or_404(Course, pk=course_id)
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = course
            comment.save()
            return redirect('courses_detail', course_id=course_id)
        return render(request, 'courses/courses_detail.html', {'course': course, 'comment_form': form})


