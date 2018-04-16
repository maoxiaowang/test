from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request, 'dashboard/index.html')