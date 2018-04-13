from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import ListView

# Create your views here.


class ComputeQuery(ListView):

    def get(self, request, *args, **kwargs):
        return HttpResponse()