from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def user_logged_in(request):
    return HttpResponse("User logged in successfully")
