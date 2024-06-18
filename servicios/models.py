from django.db import models

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.ImageField(upload_to='servicios/')
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion