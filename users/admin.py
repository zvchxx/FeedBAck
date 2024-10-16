from django.contrib import admin

from users.models import ProfileUserModel

@admin.register(ProfileUserModel)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('id',  'email', 'created_at',)
    ordering = ('created_at',)
    search_fields = ('name', 'id')
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)