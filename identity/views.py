# coding=utf-8
import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import get_user_model, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods, require_GET
from identity.forms import *
from identity.constants import *
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()
logger = logging.getLogger('default')


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
        logger.debug('login page')
        form = self.authentication_form(initial=self.initial, auto_id=True)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        context = {}
        form = self.authentication_form(data=request.POST, auto_id=True,
                                        error_class=UlErrorList)
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
    # @permission_required('auth.create')
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, auto_id=True,
                               error_class=UlErrorList)
        if form.is_valid():
            username = form.cleaned_data['username']
            self.model().create_user(
                username,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            messages.add_message(request, messages.SUCCESS,
                                 _('You have registered successfully, '
                                   'please login.'))
            return HttpResponseRedirect(reverse('identity:user_login'))
        else:
            return render(request, self.template_name, {'form': form})


class UserUpdate(UpdateView):

    model = UserModel
    form_class = UserUpdateForm
    template_name = ''

    # @permission_required('auth.update')
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)


# @method_decorator(login_required, name='dispatch')
class UserDelete(DeleteView):

    model = UserModel

    # @permission_required('auth.delete')
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)


# @method_decorator(login_required, name='dispatch')
class UserDetail(DetailView):

    model = UserModel
    template_name = 'identity/user_detail.html'

    extra_context = {}

    # @permission_required('auth.detail')
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        user_obj = UserModel.objects.filter(username=username)
        context = {
            'username': user_obj.get('username'),
            'email': user_obj.get('email'),
            'is_active': user_obj.get('is_active')
        }
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class UserList(ListView):

    model = UserModel

    # @permission_required('identity.user_list')
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)


class GroupList(ListView):
    pass


class GroupDetail(DetailView):
    pass


class GroupsUpdate(UpdateView):

    form_class = UserGroupsUpdateForm


class PermissionList(ListView):
    pass


# # @method_decorator(login_required, name='dispatch')
# class UserPermissionUpdate(UpdateView):
#
#     form = UserPermissionUpdateForm
#     model =
#     template_name = ''
#     template_name_field = ['permissions']
#
#
# # @method_decorator(login_required, name='dispatch')
# class GroupPermissionUpdate(UpdateView):
#
#     form = GroupPermissionUpdateForm
#     model = Permission
#     template_name = ''
#     template_name_field = ['permissions']


@method_decorator(login_required, name='dispatch')
class PasswordChange(auth_views.PasswordChangeView):
    """
    Change password by providing current password
    """

    template_name = 'identity/password_change.html'


@method_decorator(login_required, name='dispatch')
class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    """
    Change password done
    """
    template_name = 'identity/password_change_done.html'


@method_decorator(login_required, name='dispatch')
class PasswordReset(auth_views.PasswordResetView):
    """
    Validate and send a password reset email
    """
    pass


@method_decorator(login_required, name='dispatch')
class PasswordResetDone(auth_views.PasswordResetDoneView):
    """
    Email has been sent
    """
    pass


@method_decorator(login_required, name='dispatch')
class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    """
    Authorized to set a new password
    """
    pass


@method_decorator(login_required, name='dispatch')
class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    """
    Password reset all done
    """
    pass