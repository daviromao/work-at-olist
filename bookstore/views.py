from rest_framework import viewsets

from bookstore.models import Author, Book
from bookstore.pagination import StandardResultsSetPagination
from bookstore.serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = [
        'name',
        'edition',
        'publication_year',
        'authors',
    ]