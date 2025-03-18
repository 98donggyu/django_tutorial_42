from django.shortcuts import render, redirect, get_object_or_404
from community.forms import Form
from community.models import Article
from django.urls import reverse

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        print(form)
        if form.is_valid():
            form.save() # 필드 값 저장하기
        return redirect(reverse('list'))
    else:
        form = Form()  
    return render(request, 'write.html', {'form' : form}) # request, template,

def articleList(requests):
    article_list = Article.objects.all()
    print(article_list)
    return render(requests, 'list.html', {'article_list' : article_list})

def viewDetail(request, num=1):
    article_detail = Article.objects.get(id=num)
    # article_detail = get_object_or_404_(Article, id=num)
    return render(request, 'view_detail.html', {'article_detail' : article_detail})

def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('list')  # 목록 페이지로 리다이렉트
    else:
        return redirect('view_detail', article_id=article_id)