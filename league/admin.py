from django.contrib import admin
from .models import Manager

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'contact')   # 👈 shows in table
    search_fields = ('name', 'contact')         # 👈 search option