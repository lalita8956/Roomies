from django.contrib import admin
from .models import Work, Task

admin.site.register(Work)
admin.site.register(Task)

class WorkAdmin(admin.ModelAdmin):
    pass

class TaskAdmin(admin.ModelAdmin):
    pass