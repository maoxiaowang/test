# coding=utf-8
"""
Create your views here.
"""
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import (DetailView, ListView, CreateView, UpdateView, DeleteView)
from django.http.response import JsonResponse
from common.mixin import ret_format
from django.views.decorators.http import (
    require_POST, require_http_methods)
from .tasks import create_server_task


# @require_GET
# @login_required
# @permission_required('compute.list_server', raise_exception=True)
# def server_list(request):
#     context = {}
#     page = request.GET.get('page')
#     items_per_page = str2digit(request.GET.get('items', 5), 20)
#     server_objects = Server.objects.filter()
#
#     # Pagination
#     paginator = Paginator(server_objects, items_per_page)
#     try:
#         servers = paginator.page(page)
#     except PageNotAnInteger:
#         servers = paginator.page(1)
#     except EmptyPage:
#         servers = paginator.page(paginator.num_pages)
#
#     context['servers'] = servers
#     return TemplateResponse(request, 'compute/server_list.html', context=context)
#


class ServerList(ListView):
    pass


class ServerDetail(DetailView):
    pass


class ServerCreate(CreateView):
    pass


class ServerUpdate(UpdateView):
    pass


class ServerDelete(DeleteView):
    pass


# @require_GET
# @login_required
# @permission_required('compute.detail_server')
# def server_detail(request, **kwargs):
#     # get from OpenStack later
#     uuid = kwargs.get('id')
#     compute_obj = get_object_or_404(Server, uuid)
#     return TemplateResponse(request, 'compute/server_detail.html', compute_obj)


@require_POST
@login_required
@permission_required('compute.create_server')
def server_create(request):

    # and more params
    create_server_task.delay(body=request.POST)
    return JsonResponse(ret_format(data={}))


def server_change(request):
    pass


@require_http_methods(['DELETE'])
@login_required
@permission_required('compute.delete_server')
def server_delete(request, server_id, **kwargs):
    pass


def snap_list(request):
    pass


def image_list(request):
    pass


def backup_list(request):
    pass
