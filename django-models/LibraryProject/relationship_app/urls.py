from Django urls import path
from .views import list_books

urlpatterns =[
    path('library/',LibraryDetailView.as_view().name="library.detail"),
    path('list_books/',list_books.name='list_books'),
    path('register/',views.register.as_view,name='register'),
    path('login/',views.login_view.as_view(template_name='relationship_app/login.html'),name='login'),
    path('logout/',views.logout_view.as_view(template_name='relationship_app/logout.html'),name='logout'),
]