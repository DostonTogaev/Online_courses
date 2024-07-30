from django.db import models
from courses.models import Comment
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    Body = models.TextField()
    join_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    Education = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name
