from django.contrib import admin

# Register your models here.

from courses.models import Course, Comment, Category

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Comment)