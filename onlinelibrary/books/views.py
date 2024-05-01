from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .permissions import isOwnerOrSuperUser
from .models import Book, Author, Review
from .serializers import (BookSerializer, 
                          UserSerializer, 
                          AuthorSerializer,  
                          BookDetailSerializer, 
                          ReviewDetailSerializer)
# books/
class BookView(ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', ]:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(self.__class__, self).get_permissions()

# books/<int:pk>/
class BookDetailView(ModelViewSet):

    serializer_class = BookDetailSerializer

    def get_queryset(self):
        return Book.objects.filter(id = self.kwargs['pk'])
    
    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(self.__class__, self).get_permissions()

    def update(self, request, *args, **kwargs):    
        instance = self.get_object()
        serializer = BookDetailSerializer(instance, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    
# review/
class ReviewView(ModelViewSet):
    
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(book__id = pk)

# review/<int:id>/
class ReviewDetailView(ModelViewSet):
    
    serializer_class = ReviewDetailSerializer

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            self.permission_classes = [isOwnerOrSuperUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        return Review.objects.filter(pk = self.kwargs['id'])
    
    def get_object(self):
        try:
            obj = Review.objects.get(pk = self.kwargs['id'])
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise Http404
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ReviewDetailSerializer(instance, data = request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(instance)

# author/
class AuthorBookView(ModelViewSet):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

# user/    
class UserViewSet(CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['created', 'update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(self.__class__, self).get_permissions()