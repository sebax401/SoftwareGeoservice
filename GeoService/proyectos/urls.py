from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyectos, name='proyectos'),
    path('agregarProyecto/', views.agregarProyecto, name='agregarProyecto'),
    path('crud_proyectos/', views.crud_proyectos, name='crud_proyectos'),
    path("agregarProyecto/guardar/", views.guardarProyecto, name="guardarProyecto"),

]