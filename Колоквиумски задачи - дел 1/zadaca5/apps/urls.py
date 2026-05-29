from django.urls import path

from .views import index,edit_kniga

urlpatterns=[
    path('',index,name='index'),
    path('edit/<int:id>/',edit_kniga,name='edit_kniga'),
]
