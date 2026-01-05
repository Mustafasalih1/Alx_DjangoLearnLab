from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import BookSerializer, AuthorSerializer
from . models import Book , Author
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated
from diango_filter.rest_framework import DjangoFilterBackend
from rest_framework import filters

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchField, filters.OrderingFolter]
    filterset_fields = ['tilte', 'author']
    search_fields = ['title', 'author_name']
    ordering_fields = ['tite' , 'publication_yera']
    ordering = ['title']
    
class BookDetailView(generics.RetriveeAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchField, filters.OrderingFolter]
    filterset_fields = ['tilte', 'author']
    search_fields = ['title', 'author_name']
    ordering_fields = ['tite' , 'publication_yera']
    ordering = ['title']
    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['pk'])
    
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['pk'])

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['pk'])