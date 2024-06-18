from django.shortcuts import render
from .models import Servicio
# Create your views here.


def listar_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/listar_servicios.html', {'servicios': servicios})