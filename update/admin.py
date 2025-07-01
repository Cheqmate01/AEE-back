from django.contrib import admin
from .models import Update

# Register your models here.
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('event_theme', 'event_date')
    search_fields = ('event_theme', 'event_date')
    list_filter = ('event_date',)

admin.site.register(Update, UpdateAdmin)