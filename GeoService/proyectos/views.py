from django.http import HttpResponse
from django.template  import loader
from django.shortcuts import render
from .models import proyecto
from django.db.models import Q

# Create your views here.


def proyectos(request):

    buscar = request.GET.get('buscar', '')
    año = request.GET.get('año', '')

    proyectos = proyecto.objects.all()

    # Filtro de búsqueda
    if buscar:
        proyectos = proyectos.filter(
            Q(nombre__icontains=buscar) |
            Q(año__icontains=buscar) |
            Q(estado__icontains=buscar)
        )

    # Filtro por año
    if año:
        proyectos = proyectos.filter(año=año)

    # Obtener los años existentes
    años = proyecto.objects.values_list('año', flat=True).distinct().order_by('-año')

    return render(request, 'index.html', {
        'proyectos': proyectos,
        'buscar': buscar,
        'años': años,
        'año_seleccionado': año
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
