from django.db import models
from django.contrib.auth.models import user
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey (Author.on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Library(models.Mode1):
    name = models.CharField (max_length = 100)
    books = models.ManyToManyField (book)
    def __str__ (self):
        return self.name

class Librarian(models.Model):
    name = models.CharField (max_length = 100)
    library = models.OneToOneField (library.on_delete = models.CASCADE)
    def __str__ (self):
        return self.name

class UserProfile(models.Model):
    role = models.CharField(max_length=100), choices = [('Librarian','Librarian'),('Admin','Admin'),('Member','member')]
    user = models.OneToOneField(user,on_delete=models.CASCADE)

def create_user_profile(sender,instance,created,""kwargs):
    if created:
        userprofile.objects.create(user=instance)
        
 class Meta:
    permissions = [
            ("add_book_permission", "can_add_book"),
            ("change_book_permission", "can_change_book"),
            ("delete_book_permission", "can_delete_book"),
        ]

@permission_required('relationship_app.add_book_permission')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    return render(request, 'add_book.html')

@permission_required('relationship_app.change_book_permission')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect('book_list')
    return render(request, 'edit_book.html', {'book': book})


@permission_required('relationship_app.delete_book_permission')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')
    

