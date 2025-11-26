from django.urls import path
urlpatterns = [
     path('books/', BookList.as_view(), name='book-list')
     path('', include(router.urls))
]

