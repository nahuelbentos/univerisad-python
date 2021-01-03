from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')

    return  render(request, 'bienvenido.html', {'nro_personas': Persona.objects.count(), 'personas': personas})


def despedirse(request):
    return HttpResponse('Despedida desde Django')



def contacto(request):
    return HttpResponse('Nahuel Bentos - 098426398')
