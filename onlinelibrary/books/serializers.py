from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from .models import Book, Author, Review, User

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

    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(BookSerializer, self).to_representation(instance)
        representation['author'] = instance.author.firstname + ' ' + instance.author.lastname
        return representation

class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    reviews = ReviewSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author_model = Author.objects.get(firstname = instance.author.firstname, lastname = instance.author.lastname)
        author_model.firstname = author_data['firstname']
        author_model.lastname = author_data['lastname']
        author_model.save()
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.publish_date = validated_data.get('publish_date', instance.publish_date)
        instance.save()

        return instance


    class Meta:
        model = Book
        fields = ('title', 'author', 'reviews', 'description', 'publish_date')
