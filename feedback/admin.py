from django.contrib import admin

from feedback.models import ProblemModel, OfferModel

@admin.register(ProblemModel)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'description', 'created_at',)
    ordering = ('created_at',)
    search_fields = ('user', 'id', 'title',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)


@admin.register(OfferModel)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'description', 'created_at',)
    ordering = ('created_at',)
    search_fields = ('user', 'id', 'title',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)