from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from students.models import Student, User

# Register your models here.

admin.site.register(Student)
admin.site.register(User)
