import string
from django.utils.text import slugify

def unique_news_slug_generator(instance, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug)
 
    if qs:
        new_slug = "{slug}-{id}".format(
            slug=slug,
            id=qs.first().id
        )
        return unique_news_slug_generator(instance, new_slug=new_slug)
    return slug


def unique_category_slug_generator(instance, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug)
 
    if qs:
        new_slug = "{slug}-{id}".format(
            slug=slug,
            id=qs.first().id
        )
        return unique_category_slug_generator(instance, new_slug=new_slug)
    return slug