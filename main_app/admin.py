from django.contrib import admin
from .models import HomePage, AboutPage, Serts

class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'workname', 'header', 'topbox', 'header2', 'botbox', 'image')

admin.site.register(AboutPage)

class SertsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sert_name', 'serts')

admin.site.register(Serts)

class HomePageAdmin(admin.ModelAdmin):
    list_display = ('quote', 'text', 'photo')

admin.site.register(HomePage)