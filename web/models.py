from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# TODO: add email sender script

# TODO:

class Post(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    link = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Mail(models.Model):
    Fornavn = models.CharField(max_length=100)
    Efternavn = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Email