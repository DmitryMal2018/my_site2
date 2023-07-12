from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin) :
    list_display = ('id', 'name', 'username',)
    list_display_links = ('name', 'username')
    search_fields = ('name', 'username')
    raw_id_fields = ('username',)
    list_per_page = 5
    fieldsets = (
        ('Название команды', {
            'fields': ('name',)
        }),
        ('Внешние связи', {
            'fields': ('username',)
        }),
    )
