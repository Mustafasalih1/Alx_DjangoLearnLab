from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_member(user):
    return user.is_authenticated and user.role == "Member"

@user_passes_test(is_member)
def member_dashboard(request):
    return HttpResponse("Welcome Member! This is the Member Page.")
