from django.contrib import admin
from django.urls import path, include
from blog.views import index, blog, Blog_detailView, contact, about
urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog_detail/<int:blog_id>/', Blog_detailView.as_view(), name='blog_detail'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),


]