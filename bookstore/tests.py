from django.core.management import call_command
from django.test import TestCase
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
        
        author_results = response.data['results']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(author_results), 2)

    def test_get_author(self):
        """
        Ensure we can read author detail
        """

        url = reverse('author-detail', args=[1])
        
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], self.author_one.name)


class BookTests(APITestCase):
    def setUp(self):
        self.author_one = Author.objects.create(name='Luciano Ramalho')
        self.author_two = Author.objects.create(name='Robert C. Martin')

        self.book_one = Book.objects.create(name='Clean Code', edition=1, publication_year=2008)
        self.book_two = Book.objects.create(name='Clean Code', edition=2, publication_year=2011)

        self.author_two.books.add(self.book_one)
        self.author_two.books.add(self.book_two)
        self.author_one.books.add(self.book_two)
        
    def test_get_books(self):
        """
        Ensure we can read a book list
        """

        url = reverse('book-list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_get_book(self):
        """
        Ensure we can read a book
        """

        url = reverse('book-detail', args={1})

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['id'], self.book_one.id)
    
    def test_post_book(self):
        """
        Ensure we can create a new book object.
        """

        url = reverse('book-list')
        data = {
            'name': 'Python Fluent',
            'edition': 1,
            'publication_year': 2015,
            'authors': [1]
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], data['name'])

    def test_update_book(self):
        """
        Ensure we can update a exist book
        """

        url = reverse('book-detail', args='1')

        data = {
            'name': 'Python Book',
            'edition': 5,
            'publication_year': 2015,
            'authors': [1]
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], data['name'])
    
    def test_delete_book(self):
        """
        Ensure we can delete a exist book
        """

        url = reverse('book-detail', args='1')

        current_list_amount = Book.objects.count()

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(current_list_amount - 1, Book.objects.count())


class ImportAuthorCommandTests(TestCase):

    def test_import_author(self):
        """
        Ensure custom command test import it's working
        """

        path_file = 'bookstore/management/commands/test_import_authors.csv'
        args = [path_file]

        call_command('import_authors', *args)

        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(Author.objects.get(id=1).name, 'davi')