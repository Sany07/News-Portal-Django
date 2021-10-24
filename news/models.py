from taggit.managers import TaggableManager
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/%Y-%m-%d/', blank=True, null=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        db_table = "authors"

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=255)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')
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
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='photos/news/%Y-%m-%d/', blank=True, null=True)
    thumbnail_url = models.URLField(max_length=300, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # ratings = GenericRelation(Rating, related_query_name='ratings')
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    tags = TaggableManager()

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        db_table = "news"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("newspaper:single-post", kwargs={'slug': self.slug})

    # @property
    def get_comment_count(self):
        # comment_count = News.objects.all().annotate(Count('post__id')).order_by('-post__id__count')
        comment_count = self.post.values(
            'post__id').aggregate(models.Count('post__id'))
        return comment_count['post__id__count']

    #
