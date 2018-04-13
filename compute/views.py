from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from common.decorators import request_method
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from compute.models import ComputeModel

# Create your views here.


# @request_method('GET')
# @login_required
# @permission_required('compute.list', raise_exception=True)
# def compute_list(request, *args, **kwargs):
#     pass
#
#
# @request_method('POST')
# @login_required
# @permission_required('compute.detail')
# def compute_detail(request, *args, **kwargs):
#     pass


@method_decorator(login_required, name='dispatch')
class ComputeDetail(DetailView):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the objects
        context['compute_detail'] = ComputeModel.objects.all()
        return context


class ComputeList(ListView):

    queryset = ComputeModel.objects.all()
