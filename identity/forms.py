# coding=utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import forms as auth_forms
from django.forms.utils import ErrorList
from django.contrib.auth import get_user_model


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
        min_value=8,
        required=False
    )
    remember_me = forms.BooleanField(
        label=_('Remember me'),
        widget=forms.CheckboxInput(),
        required=False
    )
    submit_btn = _('Sign in')
    form_slogan = _('Please sign in')
    lost_password = _('Lost password?')

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
                'class': 'form-control',
                'id': 'inputUsername',
                'autofocus': True,
                'placeholder': _('Username'),
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
                'class': 'form-control',
                'id': 'inputPassword1',
                'placeholder': _('Password'),
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
                'class': 'form-control',
                'id': 'inputPassword2',
                'placeholder': _('Password confirm'),
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
                'class': 'form-control',
                'id': 'inputEmail',
                'placeholder': _('Email Address'),
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
    submit_btn = _('Register')
    form_slogan = _('Please Register')

    class Meta:
        model = get_user_model()
        fields = ("username",)

    def clean_username(self):
        # Just an example of cleaning a specific filed attribute
        # cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        for i in '!@#$%^&*':
            if i in username:
                raise forms.ValidationError
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
