from django.contrib import admin
from .models import *
# Register your models here.

class AvtorAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
       return request.user.is_superuser
class KnigaAdmin(admin.ModelAdmin):
    search_fields = ["opis"]
    def has_add_permission(self, request):
        return request.user.is_superuser or Avtor.objects.filter(email=request.user.email).exists()
    def save_model(self, request, obj, form, change):
        super().save_model(request,obj,form,change)
        avtor = Avtor.objects.filter(email=request.user.email).first()
        if avtor:
         obj.avtori.add(avtor)
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        if request.user.is_superuser:
            return True
        return obj.avtor.email == request.user.email
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs
        return qs.filter(
            avtori__email=request.user.email
        ).exclude(
            opis=""
        )
admin.site.register(Kniga,KnigaAdmin)
admin.site.register(Avtor,AvtorAdmin)
admin.site.register(Kupuvac)