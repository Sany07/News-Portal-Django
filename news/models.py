from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True,null=True, blank=True, max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',blank=True, null=True ,on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=250,blank=False)
    slug = models.SlugField(unique=True,null=True, blank=True, max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='photos/news/%Y-%m-%d/')
    timestamp = models.DateTimeField(auto_now_add=True)
    # ratings = GenericRelation(Rating, related_query_name='ratings')
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    # instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor')

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        db_table = "news"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("courses:single-course", kwargs={'slug': self.slug})

