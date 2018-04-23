# coding=utf-8
"""
Create your views here.
"""
from django.contrib.auth.decorators import login_required
from common.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from compute.models import Compute
from django.template.response import TemplateResponse
from common.utils.string_ import str2digit
from common.openstack.compute import ComputeRequest
from django.views.decorators.http import require_GET, require_POST


@require_GET
@login_required
@permission_required('compute.list')
def server_list(request):
    context = {}
    page = request.GET.get('page')
    items_per_page = str2digit(request.GET.get('items', 5), 20)
    compute_objects = Compute.objects.filter()

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


@require_GET
@login_required
@permission_required('compute.detail')
def server_detail(request, **kwargs):
    # get from OpenStack later
    uuid = kwargs.get('id')
    compute_obj = get_object_or_404(Compute, uuid)
    return TemplateResponse(request, 'compute/detail.html', compute_obj)


@require_POST
@login_required
@permission_required('compute.create')
def server_create(request):
    name = request.POST.get('name')
    # and more params
    ComputeRequest(request).compute_create(name)


