from django.contrib import admin

from .models import SiteSettings, HomePageSettings


admin.site.register(SiteSettings)
admin.site.register(HomePageSettings)

