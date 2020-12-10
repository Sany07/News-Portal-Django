from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL

# from comment.models import Comment
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True,null=True, blank=True, max_length=255)
    parent = models.ForeignKey('self',blank=True, null=True ,on_delete=models.CASCADE, related_name='children')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("newspaper:category", kwargs={'slug': self.slug})



class News(models.Model):
    title = models.CharField(max_length=250,blank=False)
    slug = models.SlugField(unique=True,null=True, blank=True, max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='photos/news/%Y-%m-%d/')
    timestamp = models.DateTimeField(auto_now_add=True)
    # ratings = GenericRelation(Rating, related_query_name='ratings')
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    # instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    tags = TaggableManager()

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        db_table = "news"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("newspaper:single-post", kwargs={'slug': self.slug})

    def get_comment_count(self):
        # comment_count = News.objects.all().annotate(Count('post__id')).order_by('-post__id__count') 
        most_commented= self.post.values('post__id').aggregate(models.Count('post__id'))
        
        return most_commented['post__id__count']