# coding=utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import forms as auth_forms
from django.forms.utils import ErrorList


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return ('<div class="form-error-list">%s</div>' %
                ''.join(['<div class="form-error">%s</div>' % e for e in self]))


class AuthenticationForm(auth_forms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    error_css_class = 'error'
    required_css_class = 'required'

    # email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={'class': 'validate'}),
    #     max_length=32,
    #     min_length=6
    # )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'validate',
                'maxlength': 32,
                'minlength': 8
            }
        ),
    )
    password_length = forms.IntegerField(
        widget=forms.HiddenInput(),
        max_value=32,
        min_value=8
    )
    keep_login = forms.BooleanField(
        widget=forms.CheckboxInput(),
        required=False
    )

    def clean_username(self):
        # Just an example of cleaning a specific filed attribute
        # cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['email']
        for i in '!@#$%^&*':
            if i in username:
                raise forms.ValidationError
        return username

    def confirm_login_allowed(self, user):
        # allow inactive user to login
        pass


class UserCreationForm(auth_forms.UserCreationForm):

    pass


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    """

    """