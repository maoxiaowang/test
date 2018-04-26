from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import TenantModel
from django.contrib.auth.decorators import permission_required

# Create your views here.


class TenantList(ListView):

    model = TenantModel
    template_name = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        pass

    @permission_required('identity.list')
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
