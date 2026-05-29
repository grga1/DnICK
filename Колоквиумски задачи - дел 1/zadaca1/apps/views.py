from django.shortcuts import render, redirect
from .models import Cake, Baker
from .forms import CakeForm
# Create your views here.

def index(request):
    cakes = Cake.objects.all()
    context = {
        'cakes':cakes
    }
    return render(request,'index.html',context)

def add_cake(request):
    if request.method == 'POST':

        form = CakeForm(request.POST,request.FILES)
        if form.is_valid():
            cake = form.save(commit=False)
            cake.baker = Baker.objects.first()
            cake.save()
        return redirect('index')
    else:
        form = CakeForm()
    context = {
            'form':form
        }
    return render(request,'add.html',context)
