from django.shortcuts import render

from blog.models import Blog, Author


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)

    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context)

def contact(request):
    return render(request, 'blog/contacts.html')

def about(request):
    return render(request, 'blog/about.html')

def author(request):
    authors = Author.objects.all()

    context = {
        'authors': authors
    }
    return render(request, 'blog/blog.html', context)