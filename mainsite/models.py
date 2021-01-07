from django.db import models
from django.shortcuts import reverse
from news.models import News, Category


class SiteSettings(models.Model):
    sitename = models.CharField(max_length=250,blank=False)


    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"
        db_table = "sitesettings"

    def __str__(self):
        return self.sitename

class HomePageSettings(models.Model):
    hot_news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='hot_news')
    post_catalog_one = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_one')
    post_catalog_two = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_two')
    post_catalog_three = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_three')
    post_catalog_four = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_four')
    post_catalog_five = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_catalog_five')

    class Meta:
        verbose_name = "Home Page Setting"
        verbose_name_plural = "Home Page Settings"
        db_table = "homepagesettings"

    def __str__(self):
        return self.hot_news.title

class SocialSetting(models.Model):
    icon = models.CharField(max_length=20)
    url = models.URLField(blank=False, null=False)


    class Meta:
        verbose_name = "Social Setting"
        verbose_name_plural = "Social Settings"
        db_table = "socialsettings"

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("newspaper:category", kwargs={'slug': self.slug})