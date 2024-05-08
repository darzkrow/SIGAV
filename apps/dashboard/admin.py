from django.contrib import admin
from .models import Profile, Oficina,  Empresa, Empleado,Cargo
# Register your models here.

admin.site.register(Profile)


@admin.register(Oficina)
class GestionOficina(admin.ModelAdmin):
    list_display = ('noficina',)
    list_display_links = ('noficina',)
@admin.register(Empleado)
class GestionEmpleado(admin.ModelAdmin):
    list_display = ('cedemp',)
    list_display_links = ('cedemp',)
@admin.register(Empresa)
class GestionEmpresa(admin.ModelAdmin):
   list_display = ( 'id','nempresa', 'imgref', )
   list_display_links = ('nempresa',)

@admin.register(Cargo)
class GestionCargo(admin.ModelAdmin):
    list_display = ('cargo',)
    list_display_links = ('cargo',)