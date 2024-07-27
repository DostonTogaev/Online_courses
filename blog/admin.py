from django.contrib import admin

# Register your models here.
from blog.models import Blog,Author


admin.site.register(Blog)
admin.site.register(Author)