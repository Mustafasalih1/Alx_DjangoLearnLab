from models import Author,Book,Library,Librarian

def get_books_by_author(author_name,author):
    Author = Author.objects.get (name = author_name)
    books = Author.objects.filter(author=author)
    return books

def get_books_in_library(library_name):
    Library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def get_librarian_fpr_library(libarary_name):
    Librarian.objects.get(library="")
    librarian = libarary.objects.librarian
    return librarian
