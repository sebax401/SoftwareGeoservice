from django.http import HttpResponse
from django.template  import loader

# Create your views here.

def proyectos(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def agregarProyecto(request):
    template = loader.get_template('agregarProyecto.html')
    return HttpResponse(template.render())