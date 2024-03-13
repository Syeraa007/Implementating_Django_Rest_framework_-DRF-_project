from django.test import TestCase

# Create your tests here.
from .models import *
from rest_framework.test import APIClient
from rest_framework import status

class BookAPITest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.book_data = {'title': 'Test Book', 'author': 'Test Author', 'publication_date': '2020-01-01'}
    
    # Testing the creation of a book through the API endpoint
    def test_create_book(self):
        response = self.client.post('/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')
    
    # Testing the update of a book through the API endpoint
    def test_get_book(self):
        response = self.client.put(f'/books/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_books(self):
        response = self.client.patch(f'/books/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_delete_books(self):
        response = self.client.delete(f'/books/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED) 