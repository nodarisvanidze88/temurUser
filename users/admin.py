from django.contrib import admin

# Register your models here.
from .models import TemurUsers

class TemurAdmin(admin.ModelAdmin):
    list_display = ("name","tel","email","registration")
    list_filter = ("name","tel","email","registration")
    search_fields = ("name","tel","email","registration")
admin.site.register(TemurUsers, TemurAdmin)

