from Django urls import path
from .views import list_books

urlpatterns =[
    path('library/',LibraryDetailView.as_view().name="library.detail"),
    path('list_books/',list_books.name='list_books'),
    path('register/',Register.as_view,name='register'),
    path('login/',LoginView.as_view(template_name='relationship_app/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'),name='logout'),
]