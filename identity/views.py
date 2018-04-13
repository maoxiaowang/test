# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from identity.forms import AuthenticationForm

# Create your views here.

from django.http import HttpResponse


class LoginView(auth_views.LoginView):

    template_name = 'identity/login.html'
    # redirect_field_name = 'next'  # default
    authentication_form = AuthenticationForm

    # A dictionary of context data that will be added to
    # the default context data passed to the template.
    extra_context = {}

    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.authentication_form(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.authentication_form(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class LogoutView(auth_views.LogoutView):

    def post(self, request, *args, **kwargs):
        pass




# class MyFormView(View):
#     form_class = MyForm
#     initial = {'key': 'value'}
#     template_name = 'form_template.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/success/')
#
#         return render(request, self.template_name, {'form': form})

