import status as status
from django.urls import reverse
from rest_framework.test import APITestCase


from store.models import Book
from store.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='Test book 1', price=25)
        book_2 = Book.objects.create(name='Test book 2', price=30)
        url = reverse('book-list')

        response = self.client.get(url)
        serialize_data = BooksSerializer([book_1, book_2], many=True).data
        self.assertEqual(serialize_data, response.data)