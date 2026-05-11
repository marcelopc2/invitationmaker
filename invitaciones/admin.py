from django.contrib import admin
from .models import Invitacion

@admin.register(Invitacion)
class InvitacionAdmin(admin.ModelAdmin):
    list_display = ('titulo_landing', 'slug', 'fecha_evento')
    prepopulated_fields = {'slug': ('titulo_landing',)}
