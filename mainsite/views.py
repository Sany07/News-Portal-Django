from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'site/pages/index.html'


class SinglePage(TemplateView):
    template_name = 'site/pages/single.html'

class BlogPage(TemplateView):
    template_name = 'site/pages/blog.html'

class CategoryPage(TemplateView):
    template_name = 'site/pages/category.html'



