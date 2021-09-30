from django.contrib import admin
from .models import Project, Pledge

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_filter = ("owner", "is_open")
    list_display = ("title", "description", "goal", "date_created")
admin.site.register(Project, ProjectAdmin)

class PledgeAdmin(admin.ModelAdmin):
    list_display = ("amount", "project", "supporter")
    list_filter = ("project", "anonymous")
admin.site.register(Pledge, PledgeAdmin)

