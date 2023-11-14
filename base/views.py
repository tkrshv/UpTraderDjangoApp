from django.shortcuts import render
from django.views.generic import TemplateView


class MenuPageView(TemplateView):
    template_name = 'base/index.html'
