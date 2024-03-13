from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination 
from rest_framework.response import Response

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

    # New for error handling and validation
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.AllowAny,]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    # permission_classes = [permissions.IsAuthenticated,]
    pagination_class = CustomPagination



