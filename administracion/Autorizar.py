
from datetime import date
from administracion.models import solped
from django.contrib import admin
from django.contrib import messages

@admin.action(description="Autorizar")
def autorizarSolped(modeladmin, request, queryset):

    for query in queryset:
        if query.ESTADO == 0:
            query.ESTADO = 1
            query.save()

    messages.success(request, "La/s Solicitud/es fueron aprobadas correctamente.")

@admin.action(description="Cancelar autorizacion")
def cancelarSolped(modeladmin, request, queryset):

    for query in queryset:
        if query.ESTADO == 1:
            query.ESTADO = 0
            query.save()

    messages.success(request, "La/s solicitud/es se modificaron correctamente.")

