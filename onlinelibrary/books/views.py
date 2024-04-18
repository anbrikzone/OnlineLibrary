from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class Book(ViewSet):

    def list(self, request):
        return Response([])