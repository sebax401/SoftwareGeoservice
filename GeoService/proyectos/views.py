from django.http import HttpResponse
from django.template  import loader
from django.shortcuts import render
from .models import proyecto
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

def comprobar_proyecto(request, id):
    
    existe = proyecto.objects.filter(id=id).exists()

    return JsonResponse({
        'existe': existe
    })


def proyectos(request):

    buscar = request.GET.get('buscar', '')
    año = request.GET.get('año', '')
    estado = request.GET.get('estado', '')

    proyectos = proyecto.objects.all()

    if buscar:
        proyectos = proyectos.filter( Q(nombre__icontains=buscar) | Q(año__icontains=buscar) | Q(estado__icontains=buscar)
        )

    if año:
        proyectos = proyectos.filter(año=año)

    if estado:
        proyectos = proyectos.filter(estado=estado)


    años = proyecto.objects.values_list(
        'año',
        flat=True
    ).distinct().order_by('-año')

    
    estados = proyecto.objects.values_list('estado', flat=True).distinct().order_by('-estado')

    return render(request, 'index.html', { 'proyectos': proyectos, 'buscar': buscar, 'años': años, 'año_seleccionado': año, 'estado': estado, 'estados': estados
    })

def detalles(request, proyecto_id):
    proyecto_obj = proyecto.objects.get(id=proyecto_id)

    estados = proyecto.objects.values_list('estado', flat=True).distinct().order_by('-estado')
    años = proyecto.objects.values_list('año', flat=True).distinct().order_by('año')

    return render(request, 'detalles.html', { 'proyecto': proyecto_obj, 'años': años, 'estado': estados})

#Agrega un proyecto a la base de datos
def agregarProyecto(request):
    estados = proyecto.objects.values_list('estado', flat=True).distinct().order_by('-estado')
    años = proyecto.objects.values_list('año', flat=True).distinct().order_by('año')
    return render(request, 'agregarProyecto.html', {'años': años, 'estados': estados})

#Elmina un proyecto de la base de datos
def eliminar_proyecto(request, proyecto_id):
    context = {}
    try:
        proyecto_obj = proyecto.objects.get(id=proyecto_id)
        proyecto_obj.delete()
        context['mensaje'] = 'Proyecto eliminado correctamente.'
    except proyecto.DoesNotExist:
        context['mensaje'] = 'El proyecto no existe.'
    return render(request, 'index.html', context)


#edita los proyectos
def editar_proyecto(request, proyecto_id):
    años = proyecto.objects.values_list('año', flat=True).distinct().order_by('año')
    estados = proyecto.objects.values_list('estado', flat=True).distinct().order_by('-estado')

    if proyecto_id != "":
        proyecto_obj = proyecto.objects.get(id=proyecto_id)

    return render(request, 'editarProyecto.html', {'proyecto': proyecto_obj, 'años': años, 'estado': estados})

def actualizar_proyecto(request, proyecto_id):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        año = request.POST.get('año')
        estado = request.POST.get('estado')
        num_compra = request.POST.get('num_compra')
        monto = request.POST.get('monto')
        monto_final = request.POST.get('monto_final')

        proyecto_obj = proyecto.objects.get(id=proyecto_id)
        proyecto_obj.nombre = nombre
        proyecto_obj.descripcion = descripcion
        proyecto_obj.año = año
        proyecto_obj.estado = estado
        proyecto_obj.num_compra = num_compra
        proyecto_obj.monto = monto
        proyecto_obj.monto_final = monto_final
        proyecto_obj.save()

    return render(request, 'editarProyecto.html', {'proyecto': proyecto_obj})

def guardarProyecto(request):
    años = proyecto.objects.values_list('año', flat=True).distinct().order_by('año')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        año = request.POST.get('año')
        estado = request.POST.get('estado')
        num_compra = request.POST.get('num_compra')
        #monto = request.POST.get('monto')
        monto_final = request.POST.get('monto_final')

        proyecto_obj = proyecto(nombre=nombre, descripcion=descripcion, año=año, estado=estado, num_compra=num_compra, monto_final=monto_final)
        proyecto_obj.save()
        
        return render (request, 'agregarProyecto.html', {'años': años})

def crud_proyectos(request):
    proyect = proyectos.objects.all()
    context = {'proyectos': proyect}
    print("se ha guardado correctamente")
    return render(request, 'agregarProyecto.html', context)
