# coding=utf-8
import re
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import forms as auth_forms
from django.forms.utils import ErrorList
from django.contrib.auth import get_user_model


__all__ = [
    'UlErrorList',
    'DivErrorList',
    'AuthenticationForm',
    'UserCreationForm',
    'UserUpdateForm',
    'PasswordChangeForm',
    'UserPermissionUpdateForm',
    'UserGroupsUpdateForm',
    'GroupPermissionUpdateForm'
]


class DivErrorList(ErrorList):

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''

        return ('<div class="messages">%s</div>' %
                ''.join(['<div class="alert alert-error">%s</div>' % e for e in self]))


class UlErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''

        return ('<ul class="form-error-list">%s</ul>' %
                ''.join(['<li class="alert alert-error">%s</li>' % e for e in self]))


class AuthenticationForm(auth_forms.AuthenticationForm):
    """
    用户登录验证
    """

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    error_css_class = 'error'
    required_css_class = 'required'

    # email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={'class': 'validate'}),
    #     max_length=32,
    #     min_length=6
    # )
    username = auth_forms.UsernameField(
        label=_('Username'),
        max_length=32,
        widget=forms.TextInput(
            attrs={
                # 'class': 'form-control',
                'id': 'inputUsername',
                'autofocus': True,
                # 'placeholder': _('Username'),
                'required': True,
                'spellcheck': 'false'
            }
        ),
    )
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                # 'class': 'form-control',
                'id': 'inputPassword',
                # 'placeholder': _('Password'),
                'maxlength': 32,
                'minlength': 8,
                'required': True
            }
        ),
    )
    password_length = forms.IntegerField(
        widget=forms.HiddenInput(),
        max_value=32,
        min_value=8,
        required=False
    )
    remember_me = forms.BooleanField(
        label=_('Remember me'),
        label_suffix='',  # remove ':'
        widget=forms.CheckboxInput(
            attrs={'id': 'remember_me'}
        ),
        required=False,
    )

    def clean_username(self):
        # Just an example of cleaning a specific filed attribute
        # cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        for i in '!@#$%^&*':
            if i in username:
                raise forms.ValidationError
        return username

    def confirm_login_allowed(self, user):
        # allow inactive user to login
        pass


class UserCreationForm(auth_forms.UserCreationForm):
    """
    创建用户
    """
    username = auth_forms.UsernameField(
        label=_('Username'),
        max_length=32,
        widget=forms.TextInput(
            attrs={
                'id': 'inputUsername',
                'autofocus': True,
                'required': True
            }
        ),
        help_text=_('Enter your username.')
    )
    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'inputPassword1',
                'maxlength': 32,
                'minlength': 8,
                'required': True
            }
        ),
        help_text=_('Enter your password.')
    )
    password2 = forms.CharField(
        label=_('Password confirm'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'inputPassword2',
                'maxlength': 32,
                'minlength': 8,
                'required': True
            }
        ),
        help_text=_('Enter the same password as before, for verification.')
    )
    email = forms.EmailField(
        label=_('Email Address'),
        widget=forms.EmailInput(
            attrs={
                'id': 'inputEmail',
                'max_length': 64,
                'min_length': 8,
                'required': True
            }
        )
    )
    password_length = forms.IntegerField(
        widget=forms.HiddenInput(),
        max_value=32,
        min_value=8,
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = ("username",)

    def clean_username(self):
        # Just an example of cleaning a specific filed attribute
        # cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']

        if not re.match('^\w+$', username):
            self.add_error('username',
                           'Enter a valid username. This value may contain only letters, '
                           'numbers, and _ characters.')
        return username


class UserUpdateForm(forms.Form):
    pass


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    """
    修改密码
    """
    pass


class UserGroupsUpdateForm(forms.Form):
    """
    把用户加入到(移除出)组
    """
    groups = forms.ChoiceField()


class UserPermissionUpdateForm(forms.Form):
    username = forms.ChoiceField()
    permissions = forms.MultipleChoiceField()


class GroupPermissionUpdateForm(forms.Form):
    groupname = forms.ChoiceField()
    permissions = forms.MultipleChoiceField()
