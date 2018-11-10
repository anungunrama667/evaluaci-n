from django.db import models

# Create your models here.


class Perro(models.Model):
    codigo = models.PositiveIntegerField()
    nombre =  models.CharField(max_length=30)
    tamaño= models.CharField(max_length=10)
    peso=models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=80)
    fechaRescate = models.DateField()
    op=(('R', 'Rescatado'),('D','Disponible'),('A','Adoptado'))
    Estado= models.CharField(max_length=1, choices=op,default='D')

