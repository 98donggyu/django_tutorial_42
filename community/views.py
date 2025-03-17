from django.shortcuts import render
from community.forms import Form
from .models import Article

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        print(form)
        if form.is_valid():
            form.save() # 필드 값 저장하기
    else:
        form = Form()  
    return render(request, 'write.html', {'form' : form}) # request, template,

def articleList(requests):
    article_list = Article.objects.all()
    print(article_list)
    return render(requests, 'list.html', {'article_list' : article_list})
