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
                'class': 'form-control',
                'id': 'inputUsername',
                'autofocus': True,
                'placeholder': _('Username'),
                'required': True
            }
        ),
    )
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'inputPassword',
                'placeholder': _('Password'),
                'maxlength': 32,
                'minlength': 8,
                'required': True
            }
        ),
    )
    password_length = forms.IntegerField(
        widget=forms.HiddenInput(),
        max_value=32,
        min_value=8
    )
    remember_me = forms.BooleanField(
        label=_('Remember me'),
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
    """
    创建用户
    """
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    pass


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    """
    修改密码
    """
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)