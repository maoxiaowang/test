# coding=utf-8
import json
import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from common.exceptions import InvalidParameters
from common.mixin import JSONResponseMixin
from common.forms import DivErrorList
from identity.models import Group, Permission
from identity.forms import *
from identity.exceptions import *

logger = logging.getLogger('default')
User = get_user_model()


# Create your views here.


@method_decorator(login_required, name='dispatch')
class GroupList(PermissionRequiredMixin, ListView):

    permission_required = 'identity.list_group'
    raise_exception = True
    model = Group
    template_name = 'identity/management/group_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # render group create modal
        kwargs.update({'group_create_form': GroupCreateForm()})
        return super().get_context_data(**kwargs)


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class GroupCreate(JSONResponseMixin, PermissionRequiredMixin, CreateView):

    permission_required = 'identity.add_group'
    raise_exception = True
    form_class = GroupCreateForm
    model = Group

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, auto_id=True,
                               error_class=DivErrorList)
        if form.is_valid():
            group_name = request.POST.get('name')
            self.model.objects.create(name=group_name)
            messages.add_message(request, messages.SUCCESS,
                                 _('Group %(group)s has been successfully created.'
                                   % {'group': group_name}))
            return self.render_to_json_response()
        else:
            raise self.render_to_json_response(result=False)


@method_decorator(login_required, name='dispatch')
class GroupUpdate(JSONResponseMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'identity.change_group'
    raise_exception = True
    form_class = Group

    def post(self, request, *args, **kwargs):
        pass


@method_decorator(login_required, name='dispatch')
class GroupUserUpdate(JSONResponseMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'identity.add_group_user'
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

        messages.add_message(request, messages.SUCCESS,
                             _('Users of group %(group)s has been successfully updated.'
                               % {'group': obj.name}))

        return self.render_to_json_response(
            data=obj.user_set.all().values('username', 'email', 'is_active'))


@method_decorator(login_required, name='dispatch')
class GroupDelete(JSONResponseMixin, PermissionRequiredMixin, DeleteView):

    permission_required = 'identity.delete_group'
    raise_exception = True
    model = Group
    pk_url_kwarg = 'group_id'
    success_url = '/identity/group/'

    def post(self, request, *args, **kwargs):
        # add messages

        messages.add_message(request, messages.SUCCESS,
                             _('Group %(group)s has been successfully deleted.'
                               % {'group': self.get_object().name}))
        try:
            self.delete(request, *args, **kwargs)
        except Exception as e:
            logger.error('Group deleting error, %s' % str(e))
            raise GroupDeletingError
        # TODO: also need to remove all users out of the group
        return self.render_to_json_response()


@method_decorator(login_required, name='dispatch')
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

        messages.add_message(request, messages.SUCCESS,
                             'Group %(group)s permissions has been successfully updated.'
                             % {'group': obj.name})
        return self.render_to_json_response()
