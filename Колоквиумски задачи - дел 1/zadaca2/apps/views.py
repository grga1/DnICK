from django.shortcuts import render, redirect
from .models import Travel,TourGuide
from .forms import TravelForm
# Create your views here.

def index(request):
    travels = Travel.objects.all()
    context = {
        'travels':travels
    }
    return render(request,'index.html',context)

def add_Travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST,request.FILES)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.tourGuide = TourGuide.objects.first()
            travel.save()
        return redirect('index')
    else:
        form = TravelForm()
        context = {
            'form':form
        }
    return render(request,'add.html',context)