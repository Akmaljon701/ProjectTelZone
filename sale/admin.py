from django.contrib import admin
from sale.forms import SaleAdminForm
from sale.models import Sale


class SaleAdmin(admin.ModelAdmin):
    form = SaleAdminForm
    list_display = ('id', 'produkt', 'klient', 'prodannaya_tsena', 'data')
    list_display_links = ('produkt', 'klient', 'prodannaya_tsena', 'data')
    search_fields = ('product__name', 'client__FIO', 'client__phone_number', 'sold_price', 'date')
    list_filter = ['date']
    autocomplete_fields = ['product', 'client']

    def produkt(self, obj):
        return obj.product

    def klient(self, obj):
        return obj.client

    def prodannaya_tsena(self, obj):
        return obj.sold_price

    def data(self, obj):
        return obj.date

    produkt.short_description = "Продукт"
    klient.short_description = "Клиент"
    prodannaya_tsena.short_description = 'Проданная цена'
    data.short_description = 'Дата'

    def save_model(self, request, obj, form, change):
        product = obj.product
        product.count -= 1
        if product.count == 0:
            product.status = 'sold'
        product.save()
        obj.save()


admin.site.register(Sale, SaleAdmin)
