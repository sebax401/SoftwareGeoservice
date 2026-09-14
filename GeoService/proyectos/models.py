from django.db import models

# Create your models here.

class proyecto(models.Model):

    ESTADOS = [
        ('Ejecucion', 'En ejecución'),
        ('Progreso', 'En progreso'),
        ('Terminado', 'Terminado'),
        ('Cancelado', 'Cancelado'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    año = models.IntegerField()
    estado = models.CharField(max_length=50, choices=ESTADOS)
    num_compra = models.IntegerField()
    monto = models.IntegerField(default=0)
    monto_final = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

