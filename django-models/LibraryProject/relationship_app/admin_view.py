from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm

def is_admin(user):
    return user.userprofile.role == 'admin'

@user_pass_test(is_admin)
def admin_view(request):
    return render(request,'relationship_app/admin_view.hyml')
