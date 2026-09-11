from django.http import HttpResponse
from django.template  import loader
from django.shortcuts import render
from .models import proyecto

# Create your views here.


def proyectos(request):
    proyectos = proyecto.objects.all()

    años = proyecto.objects.values_list('año', flat=True).distinct().order_by('año')
    buscar = request.GET.get('buscar')
    if buscar:
        proyectos = proyecto.objects.filter(
            nombre__icontains=buscar
        )
    else:
        proyectos = proyecto.objects.all()

    return render(request, 'index.html', {
        'proyectos': proyectos,
        'años': años,
        'buscar': buscar
    })

def detalles(request, proyecto_id):
    proyecto_obj = proyecto.objects.get(id=proyecto_id)

    años = proyecto.objects.values_list('año', flat=True).distinct().order_by('año')

    return render(request, 'detalles.html', {
        'proyecto': proyecto_obj,
        'años': años
    })

def agregarProyecto(request):
    años = proyecto.objects.values_list('año', flat=True).distinct().order_by('año')
    return render(request, 'agregarProyecto.html', {'años': años})

def guardarProyecto(request):
    años = proyecto.objects.values_list('año', flat=True).distinct().order_by('año')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        año = request.POST.get('año')
        estado = request.POST.get('estado')

        proyecto_obj = proyecto(nombre=nombre, descripcion=descripcion, año=año, estado=estado)
        proyecto_obj.save()
        
        return render (request, 'agregarProyecto.html', {'años': años})

def crud_proyectos(request):
    proyect = proyectos.objects.all()
    context = {'proyectos': proyect}
    print("se ha guardado correctamente")
    return render(request, 'agregarProyecto.html', context)
