from django.contrib import admin
from .models import TaskModel

@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['summary', 'description', 'assignee']
    readonly_fields = ['created_at', 'updated_at']


# Register your models here.
