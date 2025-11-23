from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ( "title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author")
admin.site.register(Book,BookAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('email', 'date_of_birth', 'profile_photo', 'is_admin')
    list_filter = ('is_admin', 'date_of_birth')


    fieldsets = (
        (None,{'fields': ('email', 'password')}),
        ("permission",{'fields': ('is_admin')}),
        ('personal info'), {'fields': ('date_of_birth','profile_photo')},
    )
search_fields = ('email', 'date_of_birth')
ordring = ('email')

       
     

    
        
    

admin.site.register(CustomUser, CustomUserAdmin)