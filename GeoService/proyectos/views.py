from django.http import HttpResponse
from django.template  import loader
from django.shortcuts import render
from .models import proyecto

# Create your views here.

def proyectos(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def agregarProyecto(request):
    template = loader.get_template('agregarProyecto.html')
    return HttpResponse(template.render())

def crud_proyectos(request):
    proyect = proyectos.objects.all()
    context = {'proyectos': proyect}
    print("se ha guardado correctamente")
    return render(request, 'agregarProyecto.html', context)
