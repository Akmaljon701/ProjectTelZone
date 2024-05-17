from django.contrib import admin
from client.forms import ClientAdminForm
from client.models import Client


class ClientAdmin(admin.ModelAdmin):
    form = ClientAdminForm
    list_display = ('id', 'fio', 'nomer_telefona')
    list_display_links = ('fio', 'nomer_telefona')
    search_fields = ('FIO', 'phone_number')
    ordering = ['FIO']

    def fio(self, obj):
        return obj.FIO

    def nomer_telefona(self, obj):
        return obj.phone_number

    fio.short_description = "Ф.И.О"
    nomer_telefona.short_description = "Номер телефона"


admin.site.register(Client, ClientAdmin)
