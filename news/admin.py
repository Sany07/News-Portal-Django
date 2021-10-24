from django.contrib import admin

from .models import *


admin.site.register(Category)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'is_published')


admin.site.register(News, NewsAdmin)
admin.site.register(Author)
