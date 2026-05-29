import random

from django.contrib import admin
from django.db.models import Sum, Count
from pyexpat.errors import messages

from .models import *
# Register your models here.

class BakerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
      return request.user.is_superuser

    def has_change_permission(self, request, obj = None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs.annotate(
                broj_torti = Count("cakes")
            ).filter(
                broj_torti__lt=5
            )
        return qs

class CakeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        vkupna_cena = Cake.objects.filter(baker=obj.baker).exclude(id=obj.id).aggregate(
            Sum("price")
        )["price__sum"] or 0
        if vkupna_cena+obj.price>10000:
            self.message_user(
                request,"Вкупната цена на тортите на еден пекар не смее да надминува 10 000.",level=messages.ERROR)
            return
        broj_torti = Cake.objects.filter(baker = obj.baker).count()

        if not change and broj_torti>=10:
            self.message_user(request,"Еден пекар може да има максимум 10 торти во дадено време.",level=messages.ERROR)
            return
        super().save_model(request,obj,form,change)

    def delete_model(self, request, obj):
        other_bakers = Baker.objects.exclude(id = obj.id)
        for cake in Cake.objects.filter(baker=obj):
            cake.baker = random.choice(list(other_bakers))
            cake.save()

        obj.delete()

    def has_view_permission(self, request, obj = None):
        return True
    def has_change_permission(self, request, obj = None):
        if obj is None:
            return True
        if request.user.is_superuser:
            return True

        return obj.baker.email == request.user.email

admin.site.register(Cake,CakeAdmin)
admin.site.register(Baker,BakerAdmin)