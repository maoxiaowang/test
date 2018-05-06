from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views.decorators.http import require_GET
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.template.response import TemplateResponse
# Create your views here.


@require_GET
@login_required
def index(request):

    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    else:
        _next = request.GET.get('next')
        login_url = reverse('user:user_login')

        if _next:
            login_url = '%s?next=%s' % (login_url, _next)
        return HttpResponseRedirect(login_url)
