from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from blog.models import Blog, Author, Comment
from courses.models import Category, Course
from blog.forms import CommentModelForm
from teachers.models import Teacher
from django.db.models import Q



# Create your views here.

class IndexView(View):
    def get(self, request, category_id=None, *args, **kwargs):
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            blogs = category.blogs.all()
        else:
            blogs = Blog.objects.all()
            category = None

        categories = Category.objects.all()
        courses = Course.objects.all()
        teachers = Teacher.objects.all()
        context = {
            'blogs': blogs,
            'categories': categories,
            'courses': courses,
            'teachers': teachers,
            'category': category,
        }
        return render(request, 'blog/index.html', context)

class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        courses = Course.objects.all()
        categories = Category.objects.all()
        recent_blogs = Blog.objects.order_by('-join_date')[:5]
        search_query = request.GET.get('search', '')

        if search_query:
            try:
                date_query = datetime.strptime(search_query, '%Y-%m-%d')
                blogs = Blog.objects.filter(
                    Q(title__icontains=search_query) | Q(join_date__date=date_query)
                )
            except ValueError:
                blogs = Blog.objects.filter(
                    Q(title__icontains=search_query)
                )
        paginator = Paginator(blogs, 2)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            'blogs': blogs,

            'courses': courses,
            'categories': categories,
            'recent_blogs': recent_blogs,
            'page_obj': page_obj
        }
        return render(request, 'blog/blog.html', context)


class Blog_detailView(View):
    def get(self, request, blog_id,):
        blog = Blog.objects.get(pk=blog_id)
        comments = Comment.objects.filter(blog=blog_id)
        count = blog.comments.count()
        categories = Category.objects.all()
        recent_blogs = Blog.objects.exclude(id=blog.id).order_by('-join_date')[:5]

        context = {
            'blog': blog,
            'comments': comments,
            'categories': categories,
            'recent_blogs': recent_blogs,
            'count': count
        }
        return render(request, 'blog/blog_detail.html', context)

def contact(request):
    return render(request, 'blog/contacts.html')

def about(request):
    return render(request, 'blog/about.html')

class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()

        context = {
            'authors': authors
        }
        return render(request, 'blog/blog.html', context)


class AddComment(View):
    def get(self, request, blog_id, *args, **kwargs):
        blog = get_object_or_404(Blog, id=blog_id)
        form = CommentModelForm()
        return render(request, 'blog/blog_detail.html', context={"blog": blog, "comment_form": form})

    def post(self, request, blog_id, *args, **kwargs):
        blog = get_object_or_404(Blog, id=blog_id)
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', blog_id)
        return render(request, 'blog/blog_detail.html', {'blog': blog, 'comment_form': form})


