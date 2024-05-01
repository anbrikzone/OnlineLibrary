from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    biography = models.TextField(null=True)
    
    def __str__(self) -> str:
        return self.firstname + ' ' + self.lastname

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    publish_date = models.DateField()

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    content = models.TextField()
    rating = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')