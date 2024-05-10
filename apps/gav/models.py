from django.db import models
from django.core.validators import MinLengthValidator
from apps.dashboard.models import Empleado, Cargo, Oficina

# Create your models here.


class Personas(models.Model):
    LIST_NAC = [
        ('VE', 'Venezolano'),
        ('EX', 'Extranjero'),
    ]
    Lista_status = [('F', 'FAMILIAR'),
                    ('E', 'EGRESADO'),
                    ('J', 'JUBILADO'),
                    ('C', 'CONTRATISTA'),
                    ('M', 'MISC'),
                    ]
    status = models.CharField(
        'Tipo de visitante', max_length=1, choices=Lista_status, null=False, default='M')
    nac = models.CharField('Nacionalidad', max_length=2, choices=LIST_NAC, null=True, blank=True)
    dni = models.CharField('Cedula', primary_key=True,  max_length=8,validators=[MinLengthValidator(6)])
    first_name = models.CharField('Nombre', max_length=40,validators=[MinLengthValidator(3)])
    last_name = models.CharField('Apellido', max_length=40,validators=[MinLengthValidator(3)])
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    gender = models.CharField('Género', max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = "Personas"
        verbose_name_plural = "Personas"
        ordering = ['-dni']

   
    def __str__(self):
        return f"{self.dni} "
    
class Avisitantes(models.Model):
    visitor = models.ForeignKey(Personas, on_delete=models.CASCADE)
    entry = models.DateField('Fecha del Dia')
    hours = models.TimeField('Hora de Entrada')
    hoursEx = models.TimeField('Hora de Salida', null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name='Nombre del Empleados')
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE, verbose_name='Oficina a Visitar')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name='Cargo')
    obs = models.TextField('Observaciones', max_length=140, null=True, blank=True)

    class Meta:
        verbose_name = "Listado Accesos"
        verbose_name_plural = "Listado Accesos"
        ordering = ['-entry', '-hours']

    def __str__(self):
        return f"{self.visitor.dni} {self.entry} {self.hours}"
    

    