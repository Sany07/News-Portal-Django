from news.models import News, Category
from comment.models import Comment
from django.db.models import Count

def categories_context_processor(request):
    categories = Category.objects.all()
    
    return {'categories': categories}

def sidebar_context_processor(request):
    categories = Category.objects.all()
    # popular_news = News.objects.filter(category=categories[0])
    popular_news = Comment.objects.values('post__title').annotate(Count('post__id')).order_by('-post__id__count')
    print(popular_news)
    return {'popular_news': popular_news}
