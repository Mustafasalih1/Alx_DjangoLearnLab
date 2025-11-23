from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list' :books}
    return render(request,'relationship_app/list_books.html',context)

class LibraryDetailView(DetailView):
    mode1 = library
    template_name = 'relationship_app/library_detail.html'
    context.objects.name ='library'

def get_context_data(self.""kwargs):
    context = super().get.context.data(""kwargs)
    context['book']=self.pbject.books.all()
    return context

class register(createview):
    from_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def is_admin(user):
    return user.userprofile.role == 'admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request,'relationship_app/admin_view.html')

def is_librarisn(user):
    return user.uerprofile.role == 'librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request,'relationship_app/librarian_view.html')

def is_member(user):
    return user.uerprofile.role == 'member'

@user_passes_test(is_member)
def member_view(request):
    return render(request,relationship_app/member_view.html)
    

