
from django.dispatch import receiver
from django.db.models.signals import pre_save


from news.models import News, Category
from news.slug_generator import unique_news_slug_generator, unique_category_slug_generator

def save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_category_slug_generator(instance)

pre_save.connect(save_category_slug, sender=Category)


def save_news_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_news_slug_generator(instance)

pre_save.connect(save_news_slug, sender=News)