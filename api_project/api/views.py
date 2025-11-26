from django.shortcuts import render
from rest_framework import serializersviewsets
from .serializers import BookSerializer
from rest_framework.routers import DefaultRouter

# Create your views here.
class BookList(generics.ListAPIView):
    permission_class = [is_authenticated]
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class BookViewSet(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer

router = DefaultRouter
router.register(r'books_all', BookViewSet, basename='book_all')
