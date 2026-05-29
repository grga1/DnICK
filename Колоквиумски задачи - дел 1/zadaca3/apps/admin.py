from django.contrib import admin
from django.utils.timezone import now

from apps.models import Umetnik, UmetnickoDelo, Izlozba

# Register your models here.
class IzlozbaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return  request.user.is_superuser
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(
                datumNaZavrsuvanje__gt=now().date()
            )
        return qs
class UmetnikAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return  request.user.is_superuser

class UmetnickoDeloAdmin(admin.ModelAdmin):
      def save_model(self, request, obj, form, change):
          umetnik = Umetnik.objects.filter(
              email=request.user.email
          ).first()
          obj.umetnik = umetnik
          super().save_model(request,obj,form,change)
      def get_queryset(self, request):
          qs = super().get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(
              umetnickodelo__umetnik__email=request.user.email
          ).distinct()
      def has_view_permission(self, request, obj = None):
          return True
      def has_change_permission(self, request, obj = None):
              if obj is None:
                  return True
              if request.user.is_superuser:
                  return True
              return obj.umetnik.email == request.user.email

admin.site.register(Umetnik,UmetnikAdmin)
admin.site.register(UmetnickoDelo,UmetnickoDeloAdmin)
admin.site.register(Izlozba,IzlozbaAdmin)