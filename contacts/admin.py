from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','email','message')
    list_display_links = ('id','name','surname','email')
    list_per_page = 30


admin.site.register(Contact, ContactAdmin)