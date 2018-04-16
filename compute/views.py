# coding=utf-8
"""
Create your views here.
"""
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from compute.models import ComputeModel
from django.template.response import TemplateResponse
from common.decorators import request_method
from common.utils.string_ import str2digit
from common.openstack.compute import ComputeRequest
from django.contrib.auth.decorators import login_required


@request_method('GET')
@login_required
def compute_list(request):
    context = {}
    page = request.GET.get('page')
    items_per_page = str2digit(request.GET.get('items', 5), 20)
    compute_objects = ComputeModel.objects.filter()

    # Pagination
    paginator = Paginator(compute_objects, items_per_page)
    try:
        computes = paginator.page(page)
    except PageNotAnInteger:
        computes = paginator.page(1)
    except EmptyPage:
        computes = paginator.page(paginator.num_pages)

    context['computes'] = computes
    return TemplateResponse(request, 'compute/list.html', context=context)


@request_method('GET')
@login_required
def compute_detail(request, **kwargs):
    # get from OpenStack later
    uuid = kwargs.get('id')
    compute_obj = get_object_or_404(ComputeModel, uuid)
    return TemplateResponse(request, 'compute/detail.html', compute_obj)


@request_method('POST')
@login_required
def compute_create(request):
    name = request.POST.get('name')
    # and more params
    ComputeRequest(request).compute_create(name)


