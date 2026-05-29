from django.urls import path
from .views import index,add_Izlozba

urlpatterns=[
    path('',index,name='index'),
    path('add/',add_Izlozba,name='add_Izlozba'),
]