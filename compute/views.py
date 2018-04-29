# coding=utf-8
"""
Create your views here.
"""
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from compute.models import Server
from django.template.response import TemplateResponse
from django.http.response import JsonResponse
from common.utils.string_ import str2digit
from common.views_helper import ret_format
from django.views.decorators.http import (
    require_GET, require_POST, require_http_methods)
from .tasks import create_server_task


@require_GET
@login_required
@permission_required('compute.server_list')
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
@permission_required('compute.server_detail')
def server_detail(request, **kwargs):
    # get from OpenStack later
    uuid = kwargs.get('id')
    compute_obj = get_object_or_404(Server, uuid)
    return TemplateResponse(request, 'compute/server_detail.html', compute_obj)


@require_POST
@login_required
@permission_required('compute.server_create')
def server_create(request):

    # and more params
    create_server_task.delay(body=request.POST)
    return JsonResponse(ret_format(data={}))


def server_change(request):
    pass


@require_http_methods(['DELETE'])
@login_required
@permission_required('compute.server_delete')
def server_delete(request, server_id, **kwargs):
    pass


def host_list(request):
    pass


def host_detail(request):
    pass


def host_add(request):
    pass


def host_change(request):
    pass


def host_remove(request):
    pass


def snap_list(request):
    pass


def image_list(request):
    pass


def backup_list(request):
    pass
