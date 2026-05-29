from django.shortcuts import render, redirect
from .models import Kniga
from .forms import KnigaForm
# Create your views here.

def index(request):
    knigi = Kniga.objects.all()
    context = {
        'knigi':knigi
    }
    return render(request,'index.html',context)

def edit_kniga(request,id):
    obj = Kniga.objects.get(id=id)
    if request.method == 'POST':

        form = KnigaForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = KnigaForm(instance=obj)
    context = {
            'form':form
        }
    return render(request,'edit.html',context)