# coding=utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods, require_GET
from identity.models import PermissionModel
from identity.exceptions import *
from identity.forms import *
from identity.constants import *
from common.exceptions import UndefinedException
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _


UserModel = get_user_model()


# Create your views here.


@require_GET
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard:index'))
    else:
        _next = request.GET.get('next')
        login_url = reverse('identity:user_login')
        if _next:
            login_url = '%s?next=%s' % (login_url, _next)
        return HttpResponseRedirect(login_url)


class Login(auth_views.LoginView):

    template_name = LOGIN_TEMPLATE
    # redirect_field_name = 'next'  # default
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    # A dictionary of context data that will be added to
    # the default context data passed to the template.
    extra_context = {}
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.authentication_form(initial=self.initial, auto_id=False)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        context = {}
        form = self.authentication_form(data=request.POST, auto_id=True,
                                        error_class=DivErrorList)
        if form.is_valid():
            username = form.cleaned_data['username']

            # do something here
            context['username'] = username
            user = UserModel.objects.get(username=username)

            # log into
            login(request, user)

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

    template_name = LOGOUT_TEMPLATE

    @method_decorator(login_required, name='dispatch')
    def post(self, request, *args, **kwargs):

        # username = request.user.get('username')
        logout(request)
        # logout_then_login(request, login_url=None, extra_context=None)


# @method_decorator(login_required, name='dispatch')
class UserCreate(CreateView):

    form_class = UserCreationForm
    model = UserModel
    template_name = REGISTER_TEMPLATE

    def get_context_data(self, **kwargs):
        return {'form': self.form_class()}

    # @method_decorator(login_required, name='dispatch')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # @method_decorator(login_required, name='dispatch')
    # @permission_required('identity.create')
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            self.model().create_user(
                username,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            messages.add_message(request, messages.SUCCESS,
                                 _('You have registered successfully, please login.'))
            return render(request, LOGIN_TEMPLATE,
                          {'form': AuthenticationForm()})
        else:
            render(request, self.template_name, {'form': form})


class UserUpdate(UpdateView):

    model = UserModel
    form_class = UserUpdateForm
    template_name = ''

    # @permission_required('identity.update')
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)


# @method_decorator(login_required, name='dispatch')
class UserDelete(DeleteView):

    model = UserModel

    # @permission_required('identity.delete')
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)


# @method_decorator(login_required, name='dispatch')
class UserDetail(DetailView):

    model = UserModel
    template_name = 'identity/user_detail.html'

    extra_context = {}

    # @permission_required('identity.detail')
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        user_obj = UserModel.objects.filter(username=username)
        context = {
            'username': user_obj.get('username'),
            'email': user_obj.get('email'),
            'is_active': user_obj.get('is_active')
        }
        return render(request, self.template_name, context)


# @method_decorator(login_required, name='dispatch')
class UserList(ListView):

    model = UserModel

    # @permission_required('identity.list')
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)


class UserGroupUpdate(UpdateView):

    form_class = GroupPermissionUpdateForm


# @method_decorator(login_required, name='dispatch')
class UserPermissionUpdate(UpdateView):

    form = UserPermissionUpdateForm
    model = PermissionModel
    template_name = ''
    template_name_field = ['permissions']


# @method_decorator(login_required, name='dispatch')
class GroupPermissionUpdate(UpdateView):

    form = GroupPermissionUpdateForm
    model = PermissionModel
    template_name = ''
    template_name_field = ['permissions']


# @method_decorator(login_required, name='dispatch')
class PasswordChange(auth_views.PasswordChangeView):

    template_name = 'identity/password_change.html'


class PasswordChangeDone(auth_views.PasswordChangeDoneView):

    template_name = 'identity/password_change_done.html'
