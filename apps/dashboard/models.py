from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField('Cedula',max_length=10, unique=True)
    avatar = models.ImageField(upload_to='profiles',  default='users/default.jpg',null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name ='Perfil'
        verbose_name_plural ='Perfiles'
    
    def __str__(self):
        return f"{self.user.username} {self.user.first_name}"
    
def create_user_profiles(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
post_save.connect(create_user_profiles, sender=User)



#######################################################################################################
################## CONFIGURACION BASICA PARA LA GESTION DE VISITAS AL PERSONAL  #######################
#######################################################################################################


class Empresa(models.Model):
    nempresa = models.CharField(
        'Nombre de la empresa', max_length=60, unique=True)
    acronimo = models.CharField(
        'Acronimo', max_length=60, null=True, blank=True)
    rif = models.CharField('R.I.F', max_length=30, null=True, blank=True)
    imgref = models.ImageField(
        'Imagen de Referencia', upload_to='empresa/', null=True, blank=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nempresa
    

class Oficina(models.Model):
    noficina = models.CharField(
        'Nombre de la Oficina', max_length=60, unique=True)

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    def __str__(self):
        return self.noficina


class Cargo(models.Model):
    cargo = models.CharField('Cargo', max_length=60, unique=True)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo
    

class Empleado(models.Model):
    cedemp = models.CharField('Cedula', max_length=10,  unique=True)
    nEmp = models.CharField('Nombre', max_length=60)
    aEmp= models.CharField(
        'Apellido', max_length=60, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'

    def __str__(self):
        return self.cedula