from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # must be filled out

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.FileField(upload_to='uploads', blank=True)  # blank = true makes it optional field
    datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
