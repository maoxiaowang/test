# coding=utf-8
"""
Create your views here.
"""
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
# from django.views.generic.edit import FormMixin
from django.views.generic.edit import CreateView, DeleteView
from compute.models import ComputeModel


@method_decorator(login_required, name='dispatch')
class ComputeDetail(DetailView):

    template_name = 'compute/detail.html'

    # write the get_context_data() to make
    # the AuthorInterestForm available to the template.
    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the objects
        context['compute_detail'] = ComputeModel.objects.all()
        return context

    @permission_required('compute.detail')
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=ComputeModel.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.book_set.all()


@method_decorator(login_required, name='dispatch')
class ComputeList(ListView):

    template_name = 'compute/list.html'
    queryset = ComputeModel.objects.all()

    @permission_required('compute.list')
    def get(self, request, *args, **kwargs):
        pass


@method_decorator(login_required, name='dispatch')
class ComputeCreate(CreateView):

    queryset = None

    @permission_required('compute.create')
    def post(self, request, *args, **kwargs):
        pass


@method_decorator(login_required, name='dispatch')
class ComputeDelete(DeleteView):

    # write this
    queryset = None

    # rewrite delete method
    @permission_required('compute.delete')
    def delete(self, request, *args, **kwargs):
        # Call the base implementation or not
        super().delete(request, *args, **kwargs)
        # Do something here
        pass
