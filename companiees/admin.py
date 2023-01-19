from django.contrib import admin
from .models import Companie

class CompanieAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_published')
    list_display_links = ('id','name')
    list_per_page = 30

admin.site.register(Companie, CompanieAdmin)