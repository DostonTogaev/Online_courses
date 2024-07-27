from django.db import models
from courses.models import Comment, Course
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='teachers/')
    description = models.TextField()
    specialty = models.CharField(max_length=100)
#    comment = models.ManyToManyField(Comment)
#    course = models.ManyToManyField(Course, related_name='teacher')

    def __str__(self):
        return self.name

