from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from news.models import Category, News

class HomeView(TemplateView):
    template_name = 'site/pages/index.html'


class SingleView(TemplateView):
    template_name = 'site/pages/single.html'

class BlogView(TemplateView):
    template_name = 'site/pages/blog.html'

class CategoryView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'site/pages/category.html'

    # def get_queryset(self):
    #     return super().get_queryset().filter(is_published='True').order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.filter(category = self.object.id, is_published = True).order_by('-id')             

        return context
    




