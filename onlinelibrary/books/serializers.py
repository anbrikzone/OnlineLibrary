from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from .models import Book, Author, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['firstname', 'lastname']

class ReviewSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        representation = super(ReviewSerializer, self).to_representation(instance)
        representation['user'] = instance.user.username
        return representation

    class Meta:
        model = Review
        fields = ['user', 'rating', 'content']

class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        representation = super(ReviewDetailSerializer, self).to_representation(instance)
        representation['book'] = instance.book.title
        representation['user'] = instance.user.username
        return representation

    class Meta:
        model = Review
        fields = ('id', 'rating', 'content', 'book', 'user')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=False)

    class Meta:
        model = Book
        fields = '__all__'

class BookUpdateSerializer(serializers.ModelSerializer):

    lastname = serializers.SlugRelatedField(queryset=Author.objects, slug_field='lastname', many=True)
    
    class Meta:
        model = Book
        fields = ['title', 'lastname', 'description', 'publish_date']

class BookDetailSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = AuthorSerializer()
    reviews = ReviewSerializer(many=True)
