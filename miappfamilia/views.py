from django.shortcuts import render
from miappfamilia.models import Datos_familia

def familia(request):
    datos = Datos_familia.objects.all()
    return render(request,'miappfamilia/index_familia.html', {"datos":datos})

