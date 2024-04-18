from django.db import models
from django.conf import settings

class Author(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    biography = models.TextField()

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    description = models.TextField()
    publish_date = models.DateField()

class Review(models.Model):
    content = models.TextField()
    rating = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)