# coding=utf-8
from django.forms.utils import ErrorDict
import json


def form_errors_to_list(errors):
    assert isinstance(errors, ErrorDict)
    return [item[0]['message'] for item in list(json.loads(errors.as_json()).values())]
