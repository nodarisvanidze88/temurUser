from django.contrib import admin

# Register your models here.
from .models import TemurUsers, Courses

class TemurAdmin(admin.ModelAdmin):
    list_display = ("name","tel","email","registration","course")
    list_filter = ("registration","course")
    search_fields = ("name","tel","email","registration","course")
admin.site.register(TemurUsers, TemurAdmin)
admin.site.register(Courses)

