from django.contrib import admin
from .models import Work, User

admin.site.register(Work)
admin.site.register(User)

class WorkAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass