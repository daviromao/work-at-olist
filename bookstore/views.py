from rest_framework import viewsets

from bookstore.models import Author, Book
from bookstore.serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
