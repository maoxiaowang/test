from django import forms
from common.models.utils import get_resource_model

Resource = get_resource_model()


class VolumeCreationForm(forms.ModelForm):
    """
    创建用户
    """
    pass

    class Meta:
        model = Resource
        fields = ("username",)
