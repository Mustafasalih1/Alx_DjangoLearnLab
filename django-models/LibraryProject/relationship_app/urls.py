from Django urls import path


urlpatterns =[
    path('library/',LibraryDetailView.as_view().name="library.detail")
    path('list_books/',list_books.name='list_books')
]