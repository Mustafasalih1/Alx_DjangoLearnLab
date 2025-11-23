from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_librarian(user):
    return user.is_authenticated and user.role == "Librarian"

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return HttpResponse("Welcome Librarian! This is the Librarian Dashboard.")
