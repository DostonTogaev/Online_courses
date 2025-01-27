from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    class RatingChoices(models.TextChoices):
        Zero = '0'
        One = '1'
        Two = '2'
        Three = '3'
        Four = '4'
        Five = '5'

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    rating = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Zero.value)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='comments')
    file = models.FileField(upload_to='media/comments')
    is_active = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} => by comment'


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    number_of_students = models.IntegerField(default=0)
    number_of_ratings = models.IntegerField(default=0)
    price = models.FloatField()
    duration = models.IntegerField()
    teachers = models.ManyToManyField('teachers.Teacher', related_name='courses')
    video = models.FileField(upload_to='media/courses')
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)

    def get_teachers(self):
        return ", ".join([teacher.name for teacher in self.teachers.all()])

    get_teachers.short_description = 'Teachers'

    @property
    def hours(self):
        if self.duration >= 60:
            hours = self.duration // 60
            return hours

    @property
    def minutes(self):
        if self.duration >= 60:
            minutes = self.duration % 60
            return minutes


    def __str__(self):
        return self.title
