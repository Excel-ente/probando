from django.db import models

class solped(models.Model):
    NUMERO = models.CharField(max_length=50,null=False, blank=False)
    FECHA = models.DateField(null=True, blank=True)
    ARTICULO = models.CharField(max_length=255, null=True, blank=True)
    SECRETARIA_NUMERO = models.CharField(max_length=255, null=True, blank=True)
    SECRETARIA_NOMBRE = models.CharField(max_length=255, null=True, blank=True)
    SECRETARIA = models.CharField(max_length=255, null=True, blank=True)
    CANTIDAD = models.DecimalField(max_digits=20,decimal_places=2,default=0,null=False, blank=False)
    PRECIO = models.DecimalField(max_digits=20,decimal_places=2,default=0,null=False, blank=False)    
    TOTAL = models.DecimalField(max_digits=20,decimal_places=2,default=0,null=False, blank=False)
    DETALLE = models.TextField(null=True, blank=True) 
    CONCEPTO = models.CharField(max_length=255, null=True, blank=True)
    CATEGORIA = models.CharField(max_length=255, null=True, blank=True)
    FUENTE_FINANCIAMIENTO = models.CharField(max_length=255, null=True, blank=True)
    OBJETO_NUMERO = models.CharField(max_length=255, null=True, blank=True) 
    ESTADO = models.BooleanField(default=0)

    def __str__(self):
        NAME = str(self.NUMERO) + " - " + str(self.CONCEPTO) + " - " + str(self.TOTAL)
        return NAME
    
    class Meta:
        verbose_name = 'Solicitud de pedido'
        verbose_name_plural ='Solicitudes de pedidos' 