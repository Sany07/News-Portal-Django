from news.models import News, Category
from comment.models import Comment
from django.db.models import Count



def custom_context_processor(request):
    try:
        categories = Category.objects.all()[:6]
        news_list = News.objects.all()
        popular_news = news_list.filter(category=categories[0]).annotate(Count('post__id')).order_by('-id')
        most_commented = news_list.annotate(Count('post__id')).order_by('-post__id__count')[:4]    
        return {'categories': categories, 'popular_news':popular_news, 'most_commented': most_commented}
    
    except:
        return {'categories': None, 'popular_news':None, 'most_commented': None}