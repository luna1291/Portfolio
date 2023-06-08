from django.contrib import admin
from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_disc', 'text', 'attach', 'photo_link')


admin.site.register(Projects)
