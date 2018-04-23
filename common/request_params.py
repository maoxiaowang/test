# coding=utf-8
"""
通过提交的POST数据与标准数据对比，来校验Post参数的合法性

例如：

"""


def check_params(standard_params):

    def wrapper(func):
        def params_checker(request, *args, **kwargs):
            if request.method != 'POST':
                raise ValueError('check_params can only be used with POST method')
            # TODO: check params
            # https://github.com/Julian/jsonschema
            return func(request, *args, **kwargs)
        return params_checker

    return wrapper