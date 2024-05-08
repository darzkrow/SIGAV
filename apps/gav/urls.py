from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name='index'),
        path('search/', views.SearchPerson, name='search'),
        path('person/list/',views.lperson,name='lperson'),
        path('person/create/',views.cperson,name='cperson'),
        path('person/<str:dni>/',views.dperson,name='dperson'),
        path('person/<str:dni>/edit',views.eperson,name='eperson'),

    ]