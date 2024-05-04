from django.contrib import admin
from .models import Profile, Oficina,  Empresa, Empleado,Cargo
# Register your models here.

admin.site.register(Profile)

@admin.register(Empresa)
@admin.register(Oficina)
@admin.register(Empleado)
@admin.register(Cargo)
class GestionOficina(admin.ModelAdmin):
    list_display = ('noficina',)
    list_display_links = ('noficina',)