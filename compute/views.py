# coding=utf-8
"""
Create your views here.
"""
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from compute.models import Server
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
    server_objects = Server.objects.filter()

    # Pagination
    paginator = Paginator(server_objects, items_per_page)
    try:
        servers = paginator.page(page)
    except PageNotAnInteger:
        servers = paginator.page(1)
    except EmptyPage:
        servers = paginator.page(paginator.num_pages)

    context['servers'] = servers
    return TemplateResponse(request, 'compute/server_list.html', context=context)


@require_GET
@login_required
@permission_required('compute.detail')
def server_detail(request, **kwargs):
    # get from OpenStack later
    uuid = kwargs.get('id')
    compute_obj = get_object_or_404(Server, uuid)
    return TemplateResponse(request, 'compute/server_detail.html', compute_obj)


@require_POST
@login_required
@permission_required('compute.create')
def server_create(request):
    name = request.POST.get('name')
    # and more params
    ComputeRequest(request).compute_create(name)


def host_add(request):
    name = request.POST.get('name')