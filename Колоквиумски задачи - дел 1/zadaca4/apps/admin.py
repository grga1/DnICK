from django.contrib import admin
from .models import *
from django.utils import timezone
# Register your models here.


class AgentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return  request.user.is_superuser

class CharacteristicAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser
class EstateAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser or Agent.objects.filter(email = request.user.email).exists()
    def save_model(self, request, obj, form, change):
        old_obj = None
        if change:
            old_obj = Estate.objects.get(id = obj.id)

        super().save_model(request, obj, form, change)

        if change and old_obj.sold ==False and obj.sold == True:
            for agent in obj.agents.all():
                agent.sales +=1
                agent.save()

        agent = Agent.objects.filter(email = request.user.email).first()
        if agent:
            obj.agents.add(agent)
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.characteristics.count() == 0
    def has_view_permission(self, request, obj=None):
        return True
    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        if request.user.is_superuser:
            return True
        agent = Agent.objects.filter(email=request.user.email).first()
        if agent is None:
            return False
        return obj.agents.filter(id=agent.id).exists()
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(
                saleDate = timezone.now().date()
            )
        return qs
admin.site.register(Agent,AgentAdmin)
admin.site.register(Estate,EstateAdmin)
admin.site.register(Characteristic,CharacteristicAdmin)