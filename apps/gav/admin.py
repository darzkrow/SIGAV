from django.contrib import admin
from .models import Personas, Avisitantes
# Register your models here.


@admin.register(Personas)
class PersonAdmin(admin.ModelAdmin):
    list_display=('nac','dni','datos', 'last_name')
    ordering =('-dni',)
    search_fields = ('dni','datos', 'last_name')
    list_display_links =  ('dni','datos', 'last_name')
    list_per_page = 10

    fieldsets = (
        (None, {
            "fields": ( ('dni','nac'),
                ('first_name','last_name'),   
            ),
        }),
    )
   
    def datos(self, obj):
        return obj.first_name.upper() 


admin.site.register(Avisitantes)