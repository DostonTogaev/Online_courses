from django.db import models
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
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    file = models.FileField(upload_to='media/comments')
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} => by comment'


