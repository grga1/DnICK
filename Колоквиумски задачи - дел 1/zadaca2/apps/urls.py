from django.urls import path
from .views import index,add_Travel

urlpatterns=[
    path('',index,name='index'),
    path('add/',add_Travel,name='add_Travel'),
]