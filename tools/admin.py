from django.contrib import admin

from .models import ToolType, Tool, EmailList

@admin.register(ToolType)
class ToolTypeAdmin(admin.ModelAdmin):
    list_display = ('tool_type',)

@admin.register(Tool)
class ToolTypeAdmin(admin.ModelAdmin):
    list_display = ('tool_type', 'description', 'user', 'status')

@admin.register(EmailList)
class EmailListAdmin(admin.ModelAdmin):
    list_display = ('recipient',)
