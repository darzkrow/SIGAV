from django.urls import path
from . import views


urlpatterns = [

        #########################################################
        ####################  URLS DE VISITANTE #################
        #########################################################
        path('', views.home, name='index'),
        path('search/', views.SearchPerson, name='search'),
        path('person/list/',views.lperson,name='lperson'),
        path('person/create/',views.cperson,name='cperson'),
        path('person/<str:dni>/',views.dperson,name='dperson'),
        path('person/<str:dni>/edit',views.eperson,name='eperson'),

        #########################################################
        ####################  URLS DE VISITANTE #################
        #########################################################

        path('laccess', views.laccess, name='laccess'),
        path('eaccess/<int:pk>/edit', views.eaccess, name='eaccess'),
        path('raccess/person/<str:dni>/', views.raccess, name='raccess'),
        path('daccess/<int:pk>/', views.daccess, name='daccess'),
    ]