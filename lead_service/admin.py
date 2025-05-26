from django.contrib import admin

# Register your models here.
from .models import Lead
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'Source', 'Status', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('Status',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'Source', 'note', 'Status')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('created_at',),
        }),
    )
    readonly_fields = ('created_at',)
    actions = ['mark_as_contacted']