from django.contrib import admin

# Register your models here.
from blog.models import Blog, Author,Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'join_date', 'image')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'Education', 'image')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'blog', 'rating', 'created_date', 'is_active')
    list_filter = ('is_active', 'created_date')
    search_fields = ('name', 'email', 'blog')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_active=True)
