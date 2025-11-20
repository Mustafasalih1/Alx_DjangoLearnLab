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
    from_class = usercreationform
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
