from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={
        'Nombre':'Francisco',
        'Apellido':'Pagnotta',
    }
    return render(request,'index.html',context=context)

