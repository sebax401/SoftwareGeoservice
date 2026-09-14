from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyectos, name='proyectos'),
    path('agregarProyecto/', views.agregarProyecto, name='agregarProyecto'),
    path('crud_proyectos/', views.crud_proyectos, name='crud_proyectos'),
    path("guardarProyecto/", views.guardarProyecto, name="guardarProyecto"),
    path('detalles/<int:proyecto_id>/', views.detalles, name='detalles'),
    path('proyecto/<int:id>/existe/', views.comprobar_proyecto, name='comprobar_proyecto'),
]