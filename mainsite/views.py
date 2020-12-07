from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from news.models import Category, News
from taggit.models import Tag

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

class PostSingleView(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'site/pages/single.html'

    def get_related_post_by_category(self):       
        return super().get_queryset().filter(is_published='True', category = self.object.category.id).exclude(id=self.object.id).order_by('-id')   

    def get_related_post_filter_by_tag(self):
        for tag in Tag.objects.all():
            return self.get_related_post_by_category().filter(tags = tag)[:4]
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = self.get_related_post_filter_by_tag()           
        return context
    




