from django.db import models
from django.contrib.auth.models import user

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
    [
        ('can_add_book','can_add_book'),
        ('can_change_book','can_change_book'),
        ('can_delete_book','can_delete_book'),
    ]        

    

