from django.contrib import admin

# Register your models here.

from courses.models import Course, Category, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'get_teachers', 'category')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'rating', 'created_date', 'is_active')
    list_filter = ('is_active', 'created_date')
    search_fields = ('name', 'email', 'course')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_active=True)
