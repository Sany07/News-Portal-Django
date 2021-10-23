from django.contrib import admin

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','reply','user')
admin.site.register(Comment,CommentAdmin)

