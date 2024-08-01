from django.urls import path
from blog.views import IndexView, BlogView, Blog_detailView, contact, about, AddComment
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>', IndexView.as_view(), name='category_by_id'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog_detail/<int:blog_id>/', Blog_detailView.as_view(), name='blog_detail'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('add_comment/<int:blog_id>/comment', AddComment.as_view(), name='add_comment'),


]