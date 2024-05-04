from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Dashboard, name='home'),
   path('accounts/', include('allauth.urls')),
   path('accounts/profile', views.current_user_profile,name='profiles-view'),
   path('accounts/profile/<int:pk>/edit/', views.edit_profile,name='profile_detail'),
   path('accounts/profile/<int:pk>/', views.profile_detail,name='profile_detail'),
    
]