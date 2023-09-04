from django.db import models

class solped(models.Model):
    NUMERO = models.CharField(max_length=50,null=False, blank=False)
    FECHA = models.DateField(null=True, blank=True)
    OFICINA = models.CharField(max_length=255, null=True, blank=True)
    TOTAL = models.DecimalField(max_digits=20,decimal_places=2,default=0,null=False, blank=False)
    DETALLE = models.CharField(max_length=255, null=True, blank=True) 
    ESTADO = models.BooleanField(default=0)

    def __str__(self):
        NAME = str(self.NUMERO) + " - " + str(self.DETALLE) + " - " + str(self.TOTAL)
        return NAME
    
    class Meta:
        verbose_name = 'Solicitud de pedido'
        verbose_name_plural ='Solicitudes de pedidos' 