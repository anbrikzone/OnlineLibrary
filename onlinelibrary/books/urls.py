from django.urls import path, include
from .views import Book

urlpatterns = [
    path('', Book.as_view({'get': 'list'}), name='Book'),
]