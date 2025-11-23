from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return user.is_authenticated and user.role == "Admin"

@user_passes_test(is_admin)
def admin_dashboard(request):
    return HttpResponse("Welcome Admin! This is the Admin Dashboard.")