from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Dashboard, name='home'),
   path('accounts/', include('allauth.urls')),
    
]