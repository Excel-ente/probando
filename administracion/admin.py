from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from administracion.Autorizar import autorizarSolped,cancelarSolped
from administracion.models import solped

@admin.register(solped)
class solpedAdmin(ImportExportModelAdmin):
    list_display = ('registro','estado')
    list_filter = ('NUMERO','ESTADO','OFICINA','DETALLE',)
    actions = [autorizarSolped,cancelarSolped]

    def total(self, obj):
        return "💲{:,.2f}".format(obj.TOTAL)
    
    def registro(self,obj):
        return f'{obj.NUMERO} | {obj.OFICINA} | {obj.DETALLE} | {"💲{:,.2f}".format(obj.TOTAL)}'

    def estado(self, obj):
        if obj.ESTADO == 0:
            return "🔴 Pendiente"
        else:
            return "🟢 Aprobada"    
    


        