from django.urls import path

from .views import index,add_cake

urlpatterns = [
    path('index/',index,name='index'),
    path('cakes/add',add_cake,name='add_cake'),
]