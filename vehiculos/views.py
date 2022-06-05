from multiprocessing import context
from django.shortcuts import render
from vehiculos.models import Autos,Motos,Camiones

# Create your views here.


def autos(request):
    auto = Autos.objects.all()
    context={'auto':auto}
    return render(request,'autos.html',context=context)




def motos(request):
    moto = Motos.objects.all()                          
    context={'moto':moto}
    return render(request,'motos.html',context=context)




def camiones(request):
    camion = Camiones.objects.all()        
    context={'camion':camion}
    return render(request,'camionetas.html',context=context)
 