from rest_framework.viewsets import ModelViewSet, ViewSet, mixins
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User

from .permissions import isOwner
from .models import Book, Author, Review
from .serializers import (BookSerializer, 
                          UserSerializer, 
                          AuthorSerializer,  
                          BookDetailSerializer, 
                          BookUpdateSerializer, 
                          ReviewDetailSerializer, 
                          ReviewSerializer, 
                          ReviewUpdateSerializer)

class BookView(ListCreateAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(APIView):
    
    http_method_names = ['get', 'put', 'delete']

    @action(methods=['get'], detail=True)
    def get(self, request, pk):        
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookDetailSerializer(book)
        except:
            return Response("Method GET is not allowed")
    
        return Response(serializer.data)

    
    @action(methods=['put'], detail=True, permission_classes=[isOwner])
    def put(self, request, pk):
        if not pk:
            return Response("Method PUT is not allowed")
        
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response("Method PUT is not allowed")
        
        serializer = BookUpdateSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @action(methods=['delete'], detail=True)
    def delete(self, request, pk):
        if not pk:
            return Response("Method DELETE is not allowed")
        
        try:
            instance = Book.objects.get(pk=pk)
            instance.delete()
        except:
            return Response("Method DELETE is not allowed")
        
        return Response({"Book": f"Book {str(pk)} is deleted"})

class ReviewDetailView(APIView):

    # serializer_class = ReviewDetailSerializer
    # # queryset = Review.objects.all()
    # permission_classes = [isOwner]

    # def get_queryset(self):
    #     id = self.kwargs['id']
    #     return Review.objects.filter(pk = id)

    # def list(self, request, *args, **kwargs):
    #     obj = Review.objects.get(pk = kwargs['id'])
    #     self.check_object_permissions(request, obj)
    #     return super().list(request, *args, **kwargs)
    
    # def update(self, request, *args, **kwargs):
    #     print(self.get_object())
    #     return super().update(request, *args, **kwargs)
    http_method_names = ['get', 'put', 'delete']
    @action(methods=['get'], detail=True)
    def get(self, request, pk, id):        
        try:
            review = Review.objects.get(pk=id)
            serializer = ReviewDetailSerializer(review)
        except:
            return Response("Method GET is not allowed")
    
        return Response(serializer.data)
    
    @action(methods=['put'], detail=True, permission_classes=[isOwner])
    def put(self, request, pk, id):
        if not id:
            return Response("Method PUT is not allowed")
        
        try:
            review = Review.objects.get(pk=id)
        except:
            return Response("Method PUT is not allowed")
        
        serializer = ReviewUpdateSerializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ReviewView(ListAPIView):
    serializer_class = ReviewDetailSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(book__id = pk)

class AuthorBookView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class UserViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class ReviewView(APIView):
    
#     serializer_class = ReviewDetailSerializer
    
#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Review.objects.filter(book__id = pk)

#     def get_permissions(self):
#         if self.request.method == 'POST':
#             self.permission_classes = [IsAdminUser|IsAuthenticated]
#         elif self.request.method == 'DELETE':
#             self.permission_classes = [IsAdminUser|IsAuthenticated]
#         elif self.request.method == 'PUT':
#             self.permission_classes = [IsAdminUser|IsAuthenticated]
#         return super(ReviewView, self).get_permissions()
    
#     def get(self, request, *args, **kwargs):
#         serializer = ReviewDetailSerializer(self.get_queryset())
#         print(list(self.get_queryset()))
#         return Response(serializer.data, many=True)
    
#     def update(self, request, *args, **kwargs):
#         print(request)
#         id = request.get('id')
#         if not id:
#             return Response('No Id review for update')
#         instance = Review.objects.filter(pk = id)
#         serializer = ReviewDetailSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'Review': serializer.data})

# class BookDetailView(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer

#     @action(methods=['get', 'post', 'delete'], detail=True)
#     def review(self, request, pk = None):
#         queryset = Review.objects.filter(pk = pk)
#         serializer = ReviewSerializer(queryset, many=True)
#         return Response(serializer.data)

# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = []

#     @action(methods=['get', 'post', 'delete'], detail=True)
#     def review(self, request, pk = None):
#         queryset = Review.objects.filter(pk = pk)
#         serializer = ReviewSerializer(queryset, many=True)
#         return Response(serializer.data)

# class AuthorBookViewSet(ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = []

