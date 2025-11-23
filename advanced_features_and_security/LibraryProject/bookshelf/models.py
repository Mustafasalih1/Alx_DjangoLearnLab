from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class CustomUser(AbstractUser)::
    date_of_birth = models.DateField(null = True, blank = True)
    profile_photo = models.ImageField(upload_to = 'profile_pics/', null = True, blank = True)
    email = models.EmailField (unique = True)


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None, date_of_birth= None):
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth
            profile_photo = profile_photo
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, date_of_birth):
        user = self.creat_user(
            email,
            password = password,
            date_of_birth = date_of_birth,
            profile_photo = profile_photo
        )
       user_is_admin = True
       user.save(using = self_db)
       return user


       

    