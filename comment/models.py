from django.db import models
from django.shortcuts import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL

from news.models import News

class Comment(models.Model):
    comment = models.CharField(max_length=250,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True , on_delete=models.CASCADE, related_name='user')
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='post')
    reply = models.ForeignKey('self',blank=True, null=True ,on_delete=models.CASCADE, related_name='replies')

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "comments"

    def __str__(self):
        return '{}'.format(self.post.title)


