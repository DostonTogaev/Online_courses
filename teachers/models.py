from django.db import models
from courses.models import Course


# Create your models here.

class Teacher(models.Model):
    class LevelChoices(models.TextChoices):
        JUNIOR = 'JUNIOR'
        MIDDLE = 'MIDDLE'
        SENIOR = 'SENIOR'

    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey('courses.Category', on_delete=models.CASCADE)
    level = models.CharField(max_length=10, choices=LevelChoices.choices, default=LevelChoices.MIDDLE.value)

    def __str__(self):
        return self.name

