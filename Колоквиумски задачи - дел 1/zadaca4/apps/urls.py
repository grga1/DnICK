from django.urls import path

from .views import index, edit_estate


urlpatterns = [
    path('',index,name='index'),
    path('edit/<int:id>/',edit_estate,name='edit_estate'),
]
