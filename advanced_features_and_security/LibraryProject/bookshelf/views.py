from django.shortcuts import render,redirect
from django.contrib.auth.decorater import permission_required,has_permission


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_list(request,pk):
    
    return render(request, 'edit_template.html')

# Create your views here.
