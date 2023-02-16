import os

from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import MyForm, FormFromModel


class MyFormView(FormView):
    form_class = MyForm
    template_name = "page.html"

    def get(self, request, *args, **kwargs):
        print(request.GET)
        return super().get(request,  *args, **kwargs)


class ModelFormView(FormView):
    form_class = FormFromModel
    template_name = "page_models.html"
    success_url = reverse_lazy("modelform")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


