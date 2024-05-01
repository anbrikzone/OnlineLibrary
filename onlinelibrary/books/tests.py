import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from .models import Book, Author, Review
from .serializers import (BookSerializer, 
                          BookDetailSerializer, 
                          AuthorSerializer, 
                          ReviewSerializer, 
                          ReviewDetailSerializer, 
                          UserSerializer)

# initialize the APIClient app
client = Client()

class GetAllBooksTest(TestCase):

    Book.objects.create(title = 'Book One', author='Author One', description='Kind of description', publish_date='2024-4-15')
    Book.objects.create(title = 'Book Two', author='Author Two', description='Kind of description', publish_date='2024-4-20')

    def get_all_books(self):
        response = client.get(reverse())