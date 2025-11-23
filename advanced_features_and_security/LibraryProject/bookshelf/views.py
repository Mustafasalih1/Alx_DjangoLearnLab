from django.shortcuts import render,redirect
from django.contrib.auth.decorater import permission_required,has_permission


@permission_required('bookshelf.can_view', raise_exception=True)
def edit_view(request,plc):
    
     return render(request, 'edit_template.html',

# Create your views here.
