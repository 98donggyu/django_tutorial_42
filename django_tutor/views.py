from django.shortcuts import render
from community.models import Article

def index(request):
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    return render(request, 'index.html', {'latest_article_list' : latest_article_list})