# coding=utf-8
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)


class ImageList(ListView):
    pass


class ImageDetail(DetailView):
    pass


class ImageCreate(CreateView):
    pass


class ImageUpdate(UpdateView):
    pass


class ImageDelete(DeleteView):
    pass
