from django.shortcuts import render, redirect
from .models import *
from .forms import IzlozbaForm
# Create your views here.

def index(request):
    izlozbi = Izlozba.objects.all()
    context = {
        'izlozbi':izlozbi
    }
    return render(request,'index.html',context)

def add_Izlozba(request):
    if request.method == 'POST':
        form = IzlozbaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = IzlozbaForm()
    context = {
            'form':form
        }
    return render(request,'add.html',context)