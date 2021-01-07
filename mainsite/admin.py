from django.contrib import admin

from .models import SiteSettings, HomePageSettings, SocialSetting


admin.site.register(SiteSettings)
admin.site.register(HomePageSettings)
admin.site.register(SocialSetting)

