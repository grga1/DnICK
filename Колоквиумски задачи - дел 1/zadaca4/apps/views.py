from django.shortcuts import render, redirect

from .models import Estate
from .forms import EstateForm

# Create your views here.
def index(request):
    estates = Estate.objects.all()
    context = {
        'estates': estates
    }
    return render(request,'index.html',context)

def edit_estate(request, id):
  obj = Estate.objects.get(id=id)
  if request.method == 'POST':
     form = EstateForm(request.POST,request.FILES,instance=obj)
     if form.is_valid():
         form.save()
     return redirect('index')

  else:
      form = EstateForm(instance=obj)
  context = {
      'form': form
    }
  return render(request,'edit_estate.html',context)
