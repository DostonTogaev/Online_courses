from django.contrib import admin
from django.urls import path, include
from blog.views import index, blog, blog_detail, contact, about
urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog_detail/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),


]