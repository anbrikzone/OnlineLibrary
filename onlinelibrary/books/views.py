from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []

    # def list(self, request):
    #     books = Book.objects.all()
    #     serializer = BookSerializer(books, many=True)
    #     return Response({'books': serializer.data})
    
    # def update(self, request, pk):
    #     return Response([])