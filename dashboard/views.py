from django.shortcuts import render, redirect
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.

def dashboard(request):
    data = CountryData.objects.all()
    if request.method == 'POST':
        form = CountryDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
        else:
            print(form.errors)
    else:
        form = CountryDataForm()

    context = {
        'dataset' : data,
        'form' : form
    } 
    return render(request, 'dashboard.html', context)