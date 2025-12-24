
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet, CustomAuthToken 

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('token/', CustomAuthToken.as_view(), name='api_token'),
    path('', include(router.urls)),
]
 