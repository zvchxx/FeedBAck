from django.contrib import admin

from team.models import TeamModel

@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'first_name', 'last_name', 'created_at',)
    ordering = ('created_at',)
    search_fields = ('name', 'id', 'first_name',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)