from django.shortcuts import render
from community.forms import Form

# Create your views here.
def write(request):
    if request.method == 'Post':
        form = Form(request.POST)
        if form.is_valid():
            form.save() # 필드 값 저장하기
    else:
        form = Form()  
    return render(request, 'write.html', {'form' : form}) # request, template,
