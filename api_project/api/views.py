from django.shortcuts import render
from rest_framework import serializersviewsets
from .serializers import BookSerializer

# Create your views here.
class BookList(genirics, ListAPIView):
    permission_class = [is_authenticated]
    queryset = Book.objects.all()
    serializer_class = Bookserializer
