from urllib import response
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from bookstore.models import Author, Book


class AuthorTests(APITestCase):

    def setUp(self):
        self.author_one = Author.objects.create(name='Luciano Ramalho')
        self.author_two = Author.objects.create(name='Robert C. Martin')

    def test_get_authors(self):
        """
        Ensure we can read author list
        """

        url = reverse('author-list')

        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_author(self):
        """
        Ensure we can read author detail
        """

        url = reverse('author-detail', args=[1])
        
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], self.author_one.name)
