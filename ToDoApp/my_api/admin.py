from django.contrib import admin
from .models import Tasks

# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'Title', 'Completed']



admin.site.register(Tasks, TasksAdmin)