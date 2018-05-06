# coding=utf-8
import json
import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from common.exceptions import InvalidParameters
from common.views.mixin import JSONResponseMixin
from identity.models import Group, Permission
from identity.exceptions import *
from identity.forms import *

User = get_user_model()
logger = logging.getLogger('default')


# Create your views here.


class GroupList(PermissionRequiredMixin, ListView):

    permission_required = 'identity.list_group'
    raise_exception = True
    model = Group
    template_name = 'identity/management/group_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # render group create modal
        kwargs.update({'group_create_form': GroupCreateForm()})
        return super().get_context_data(**kwargs)


class GroupDetail(PermissionRequiredMixin, DetailView):

    permission_required = 'identity.detail_group'
    raise_exception = True
    model = Group
    template_name = 'identity/management/group_detail.html'
    pk_url_kwarg = 'group_id'    # used for rendering group detail modal

    def get_context_data(self, **kwargs):
        # rendering group permission modal
        all_perms = Permission.objects.all()
        cts = list()
        res = list()
        group_perms = self.object.permissions.all()
        group_perms_id_list = [item.id for item in group_perms]

        for ap in all_perms:
            if ap.content_type_id not in cts:
                cts.append(ap.content_type_id)
                res.append(
                    {'id': ap.content_type_id,
                     'name': ap.content_type.name})
            if ap.id in group_perms_id_list:
                ap.assigned = True
            else:
                ap.assigned = False

        # users in group
        group_users = self.object.user_set.all()
        group_user_ids = [u['id'] for u in group_users.values('id')]
        # users not in group
        not_group_users = User.objects.exclude(id__in=group_user_ids)

        kwargs.update({'all_perms': all_perms,
                       'perm_content_types': res,
                       'group_users': group_users,
                       'not_group_users': not_group_users})
        return super().get_context_data(**kwargs)


class GroupCreate(JSONResponseMixin, PermissionRequiredMixin, CreateView):

    permission_required = 'identity.add_group'
    raise_exception = True
    form_class = GroupCreateForm
    model = Group

    def post(self, request, *args, **kwargs):
        print('POST')
        form = self.form_class(data=request.POST, auto_id=True,
                               error_class=DivErrorList)
        if form.is_valid():
            self.model.objects.create(name=request.POST.get('name'))
            return self.render_to_json_response()
        else:
            raise self.render_to_json_response(result=False)


class GroupUpdate(JSONResponseMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'identity.change_group'
    raise_exception = True
    form_class = Group

    def post(self, request, *args, **kwargs):
        pass


class GroupUserUpdate(JSONResponseMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'identity.update_group_user'
    raise_exception = True
    model = Group
    pk_url_kwarg = 'group_id'

    def post(self, request, *args, **kwargs):
        user_ids = request.POST.get('user_ids')
        try:
            user_ids = json.loads(user_ids)
        except json.JSONDecodeError:
            raise InvalidParameters

        obj = get_object_or_404(self.model, pk=kwargs.get(self.pk_url_kwarg))

        old_user_ids = [str(i.id) for i in obj.user_set.all()]

        for oid in old_user_ids:
            if oid not in user_ids:
                # delete
                obj.user_set.remove(oid)

        for nid in user_ids:
            if nid not in old_user_ids:
                # add
                obj.user_set.add(nid)

        return self.render_to_json_response(
            data=obj.user_set.all().values('username', 'email', 'is_active'))


class GroupDelete(JSONResponseMixin, PermissionRequiredMixin, DeleteView):

    permission_required = 'identity.delete_group'
    raise_exception = True
    model = Group
    pk_url_kwarg = 'group_id'
    success_url = '/identity/group/'

    def post(self, request, *args, **kwargs):
        # add messages
        messages.add_message(request, messages.SUCCESS, _('Delete group succeeded'))
        return self.delete(request, *args, **kwargs)


class GroupPermissionUpdate(PermissionRequiredMixin, JSONResponseMixin, UpdateView):

    permission_required = 'identity.update_group_permission'
    raise_exception = True
    model = Group
    pk_url_kwarg = 'group_id'

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs.get(self.pk_url_kwarg))

        # permission id list
        new_perms = request.POST.get('checked_perms')
        if not new_perms:
            raise InvalidParameters
        try:
            checked_perms = json.loads(new_perms)
        except json.JSONDecodeError:
            raise InvalidParameters

        checked_perms = [item for item in checked_perms if item.isdigit()]
        old_perms_ids = [str(i.id) for i in obj.permissions.all()]

        for oid in old_perms_ids:
            if oid not in checked_perms:
                # delete
                obj.permissions.remove(oid)

        for nid in checked_perms:
            if nid not in old_perms_ids:
                # add
                obj.permissions.add(nid)

        return self.render_to_json_response()
