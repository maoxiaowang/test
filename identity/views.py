# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods
from identity.models import PermissionModel
from identity.exceptions import *
from identity.forms import *
from common.exceptions import UndefinedException

UserModel = get_user_model()


# Create your views here.

decorators = [never_cache, login_required]


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard:index'))
    else:
        return HttpResponseRedirect(reverse('identity:user_login'))


class Login(auth_views.LoginView):

    template_name = 'identity/login.html'
    # redirect_field_name = 'next'  # default
    authentication_form = AuthenticationForm

    # A dictionary of context data that will be added to
    # the default context data passed to the template.
    extra_context = {}

    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.authentication_form(request,
                                        initial=self.initial, auto_id=False)
        return render(request, self.template_name, {'login_form': form})

    def post(self, request, *args, **kwargs):
        ret = {}
        form = self.authentication_form(data=request.POST, auto_id=False,
                                        error_class=DivErrorList)
        if form.is_valid():
            username = form.cleaned_data['username']
            remember_me = form.cleaned_data['remember_me']
            if not remember_me:
                # session will expire on closing browser
                request.session.set_expiry(0)
            # do something here
            ret['username'] = username
        else:
            err_data = form.errors.as_data()
            pass
        return JsonResponse(ret)


# @method_decorator(login_required, name='dispatch')
class Logout(auth_views.LogoutView):

    def post(self, request, *args, **kwargs):
        UserModel.objects.create_user()


# @method_decorator(login_required, name='dispatch')
class UserCreate(CreateView):

    form_class = UserCreationForm
    model = UserModel
    template_name = 'identity/register.html'

    def get_context_data(self, **kwargs):
        return {'register_form': self.form_class()}

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
            return JsonResponse({'username': username})
        else:
            err_data = form.errors.as_data()
            if err_data.get('username'):
                raise InvalidUsernameFormat
            elif err_data.get('email'):
                raise InvalidEmailFormat
            elif err_data.get('password') or err_data.get('password_length'):
                raise InvalidPasswordFormat
            else:
                raise UndefinedException


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
