from rest_framework.routers import DefaultRouter

from bookstore.views import AuthorViewSet, BookViewSet

bookstore_router = DefaultRouter()
bookstore_router.register('authors', AuthorViewSet)
bookstore_router.register('books', BookViewSet)
