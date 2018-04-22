from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.template.response import TemplateResponse
# Create your views here.


@login_required
def index(request):

    return TemplateResponse(request, 'dashboard/index.html')
