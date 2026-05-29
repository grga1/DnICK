import random

from django.contrib import admin
from django.db.models import Sum
from django.db.models.aggregates import Count
from django.template.context_processors import request
from pyexpat.errors import messages

from .models import *
# Register your models here.

class TourGuideAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_change_permission(self, request, obj = None):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser
    def delete_model(self, request, obj):
        other_tourGuides = TourGuide.objects.exclude(id = obj.id)

        for tour in Travel.objects.filter(tourGuide=obj):
            tour.tourGuide = random.choice(list(other_tourGuides))
            tour.save()

        obj.delete()
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs.annotate(
                broj_destinaci = Count("destinations")
            ).filter(
                broj_destinaci__lt=3
            )
        return qs

class TravelAdmin(admin.ModelAdmin):
     def save_model(self, request, obj, form, change):

         vkupna_cena = Travel.objects.filter(tourGuide=obj.tourGuide).exclude(id = obj.id).aggregate(Sum("price"))["price__sum"] or 0

         if vkupna_cena+obj.price>50000:
             self.message_user(request,"Вкупната цена на дестинациите на еден туристички водач не смее да надминува 50 000.",level=messages.ERROR)
             return

         broj_destinacii = Travel.objects.filter(tourGuide=obj.tourGuide).count()
         if not change and broj_destinacii>5:
             self.message_user(
                 request,"Еден туристички водич може да има максимум 5 дестинации во дадено време",level=messages.ERROR
             )
             return
         super().save_model(request,obj,form,change)

     def has_view_permission(self, request, obj = None):
         return True
     def has_change_permission(self, request, obj = None):
         if obj is None:
             return True
         if request.user.is_superuser:
             return True
         return obj.tourGuide.email == request.user.email
admin.site.register(Travel)
admin.site.register(TourGuide,TourGuideAdmin)