# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect, JsonResponse
from identity.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from identity.models import UserModel
from identity.exceptions import *
from common.settings.openstack import OPENSTACK_TOKEN_TIMEOUT

# Create your views here.

decorators = [never_cache, login_required]


@require_http_methods(['GET', 'POST'])
class LoginView(auth_views.LoginView):

    template_name = 'identity/login.html'
    # redirect_field_name = 'next'  # default
    _form = AuthenticationForm

    # A dictionary of context data that will be added to
    # the default context data passed to the template.
    extra_context = {}

    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self._form(initial=self.initial, auto_id=True)
        return render(request, self.template_name, {'login_form': form})

    def post(self, request, *args, **kwargs):
        ret = {}
        form = self._form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            account_objects = self._form.objects.filter(username=username)
            if account_objects.count() == 1:
                account_object = account_objects[0]
                if account_object.password == password:
                    # login successfully
                    if not remember_me:
                        # session will expire on closing browser
                        request.session.set_expiry(0)
                    # set_login_session(request, account_object)
                    # login to OpenStack and record token in session here
                else:
                    raise InvalidPassword
            else:
                raise NoSuchUsername
        else:
            err_data = form.errors.as_data()
            if err_data.get('username'):
                raise InvalidUsernameFormat
            elif err_data.get('password') or err_data.get('password_length'):
                raise InvalidPasswordFormat
                # ret['message']['desc'] = errs[item][0].__str__
        return JsonResponse(ret)


@require_http_methods(['POST'])
@method_decorator(login_required, name='dispatch')
class LogoutView(auth_views.LogoutView):

    def post(self, request, *args, **kwargs):
        UserModel.objects.create_user()


@require_http_methods(['POST'])
@method_decorator(login_required, name='dispatch')
class UserCreateView(CreateView):

    _form = UserCreationForm

    def post(self, request, *args, **kwargs):
        form = self._form(request.POST)
        if form.is_valid():
            UserModel.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1'],
                form.cleaned_data['password2'],
            )
        else:
            err_data = form.errors.as_data()
            if err_data.get('username'):
                raise InvalidUsernameFormat
            elif err_data.get('email'):
                raise InvalidEmailFormat
            elif err_data.get('password') or err_data.get('password_length'):
                raise InvalidPasswordFormat


@require_http_methods(['GET'])
class UserDetailView(DetailView):

    template_name = 'identity/user_detail.html'

    extra_context = {}

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        user_obj = UserModel.objects.filter(username=username)
        context = {
            'username': user_obj.get('username'),
            'email': user_obj.get('email'),
            'is_active': user_obj.get('is_active')
        }
        return render(request, self.template_name, context)


class UserListView(ListView):
    pass


class UserDeleteView(DeleteView):
    pass





@require_http_methods(['PUT'])
@login_required
def password_reset(request):
    pass



