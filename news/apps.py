from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        from news.signals import save_news_slug, save_category_slug

