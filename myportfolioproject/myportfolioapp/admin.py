from django.contrib import admin
from .models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['time', 'name', 'email', 'phone']

admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Client)
admin.site.register(Contact, ContactAdmin)
admin.site.register(CompanySocialDetail)