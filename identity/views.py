# coding=utf-8
import json
import logging

from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from common.exceptions import InvalidParameters
from common.forms_helper import form_errors_to_list
from common.views_helper import JSONResponseMixin
from .models import Group, Permission
from .exceptions import *
from .forms import *

User = get_user_model()
logger = logging.getLogger('default')


# Create your views here.


class Login(auth_views.LoginView):

    template_name = 'identity/authentication/login.html'
    # redirect_field_name = 'next'  # default
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    # A dictionary of context data that will be added to
    # the default context data passed to the template.
    extra_context = {}
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        logger.debug('login page')
        form = self.authentication_form(initial=self.initial, auto_id=True)
        self.extra_context.update(
            {'form': form,
             'next': self.request.GET.get('next', '')}
        )
        return render(request, self.template_name, self.extra_context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = self.authentication_form(data=request.POST, auto_id=True,
                                        error_class=DivErrorList)
        if form.is_valid():
            username = form.cleaned_data['username']

            # do something here
            context['username'] = username
            user = User.objects.get(username=username)

            # log into
            login(request, user, backend='common.backends.UserAuthBackend')

            remember_me = form.cleaned_data['remember_me']
            if not remember_me:
                # session will expire on closing browser
                request.session.set_expiry(0)

            messages.add_message(request, messages.SUCCESS,
                                 'Welcome, %s' % username)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class Logout(auth_views.LogoutView):
    pass


class UserCreate(JSONResponseMixin, PermissionRequiredMixin, CreateView):

    permission_required = 'identity.create_user'
    form_class = UserCreationForm
    model = User

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, auto_id=True,
                               error_class=DivErrorList)
        if form.is_valid():
            username = form.cleaned_data['username']
            self.model().create_user(
                username,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            return self.render_to_json_response(
                messages=_('Successfully created user') + ' %s' % username)
        else:
            return self.render_to_json_response(
                result=False, messages=form_errors_to_list(form.errors))


class UserUpdate(PermissionRequiredMixin, UpdateView):

    permission_required = 'identity.update_user'
    model = User
    form_class = UserUpdateForm
    template_name = ''

    def post(self, request, *args, **kwargs):
        pass


class UserDelete(PermissionRequiredMixin, DeleteView):

    permission_required = 'identity.delete_user'
    model = User
    pk_url_kwarg = 'user_id'
    success_url = '/identity/user/'


class UserDetail(PermissionRequiredMixin, DetailView):

    permission_required = 'identity.detail_user'
    model = User
    template_name = 'identity/management/user_detail.html'
    pk_url_kwarg = 'user_id'

    extra_context = {}

    def get_context_data(self, **kwargs):
        # rendering group permission modal
        all_perms = Permission.objects.all()
        cts = list()
        res = list()
        user_perms = self.object.user_permissions.all()
        user_perms_id_list = [item.id for item in user_perms]

        for ap in all_perms:
            if ap.content_type_id not in cts:
                cts.append(ap.content_type_id)
                res.append(
                    {'id': ap.content_type_id,
                     'name': ap.content_type.name})
            if ap.id in user_perms_id_list:
                ap.assigned = True
            else:
                ap.assigned = False
        # current group's permission

        kwargs.update({'all_perms': all_perms,
                       'perm_content_types': res,
                       'user_id': self.kwargs[self.pk_url_kwarg]})
        return super().get_context_data(**kwargs)


class UserList(PermissionRequiredMixin, ListView):

    permission_required = 'identity.list_user'
    model = User
    template_name = 'identity/management/user_list.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({'user_create_form': UserCreationForm()})
        return super().get_context_data(**kwargs)


class UserPermissionUpdate(PermissionRequiredMixin, JSONResponseMixin, UpdateView):

    permission_required = 'identitiy.'

    model = User
    pk_url_kwarg = 'user_id'

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
        old_perms_id_list = [str(i.id) for i in obj.user_permissions.all()]

        for oid in old_perms_id_list:
            if oid not in checked_perms:
                # delete
                obj.user_permissions.remove(oid)

        for nid in checked_perms:
            if nid not in old_perms_id_list:
                # add
                obj.user_permissions.add(nid)

        return self.render_to_json_response()


class GroupList(PermissionRequiredMixin, ListView):

    permission_required = 'identity.list_group'
    model = Group
    template_name = 'identity/management/group_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # render group create modal
        kwargs.update({'group_create_form': GroupCreateForm()})
        return super().get_context_data(**kwargs)


class GroupDetail(PermissionRequiredMixin, DetailView):

    permission_required = 'identity.detail_group'

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

    permission_required = 'identity.create_group'
    form_class = GroupCreateForm
    model = Group

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, auto_id=True,
                               error_class=DivErrorList)
        if form.is_valid():
            self.model.objects.create(name=request.POST.get('name'))
            return self.render_to_json_response()
        else:
            raise InvalidGroupFormat


class GroupUpdate(JSONResponseMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'identity.update_group'
    form_class = Group

    def post(self, request, *args, **kwargs):
        pass


class GroupUserUpdate(JSONResponseMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'identity.update_group_user'
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

        return self.render_to_json_response()


class GroupDelete(JSONResponseMixin, PermissionRequiredMixin, DeleteView):

    permission_required = 'identity.delete_group'
    model = Group
    pk_url_kwarg = 'group_id'
    success_url = '/identity/group/'

    def post(self, request, *args, **kwargs):
        # add messages
        messages.add_message(request, messages.SUCCESS, _('Delete group succeeded'))
        return self.delete(request, *args, **kwargs)


class PermissionList(PermissionRequiredMixin, ListView):

    permission_required = 'identity.list_permission'
    model = Permission
    template_name = 'identity/management/permission_list.html'


class GroupPermissionUpdate(PermissionRequiredMixin, JSONResponseMixin, UpdateView):

    permission_required = 'identity.update_group_permission'
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


class PasswordChange(auth_views.PasswordChangeView):
    """
    Change password by providing current password
    """

    template_name = 'identity/authentication/password_change.html'


class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    """
    Change password done
    """
    template_name = 'identity/authentication/password_change_done.html'


class PasswordReset(auth_views.PasswordResetView):
    """
    Validate and send a password reset email
    """
    pass


class PasswordResetDone(auth_views.PasswordResetDoneView):
    """
    Email has been sent
    """
    pass


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    """
    Authorized to set a new password
    """
    pass


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    """
    Password reset all done
    """
    pass
