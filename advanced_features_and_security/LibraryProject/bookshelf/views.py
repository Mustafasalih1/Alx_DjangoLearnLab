from django.shortcuts import render,redirect
from django.contrib.auth.decorater import permission_required,has_permission


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create your views here.
