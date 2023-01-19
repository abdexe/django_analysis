from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','age','country','city','gender')
    list_display_links = ('id','username','email')
    list_per_page = 30

admin.site.register(CustomUser, CustomUserAdmin)