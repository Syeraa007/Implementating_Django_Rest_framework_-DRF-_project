from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination # New

# New Adding pagination
class CustomPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 10

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    # permission_classes = [permissions.IsAuthenticated,]
    # Add pagination to your views
    pagination_class = CustomPagination

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    # permission_classes = [permissions.IsAuthenticated,]
    pagination_class = CustomPagination



