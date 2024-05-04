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
