from django.contrib import admin
from client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'phone_number')
    list_display_links = ('FIO', 'phone_number')
    search_fields = ('FIO', 'phone_number')
    ordering = ['FIO']


admin.site.register(Client, ClientAdmin)
