from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import *
from .serializers import *
# New
from rest_framework.authentication import TokenAuthentication

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # New
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    # permission_classes = [permissions.IsAuthenticated,]

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # New
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    # permission_classes = [permissions.IsAuthenticated,]