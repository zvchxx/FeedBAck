from django.contrib import admin

from comment.models import CommentModel

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'feedback', 'created_at',)
    ordering = ('created_at',)
    search_fields = ('user', 'id', 'feedback',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)