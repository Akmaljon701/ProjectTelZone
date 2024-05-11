from django.contrib import admin
from sale.models import Sale


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'client', 'sold_price', 'date')
    list_display_links = ('product', 'client', 'sold_price', 'date')
    search_fields = ('product__name', 'client__FIO', 'client__phone_number', 'sold_price', 'date')
    list_filter = ['date']


admin.site.register(Sale, SaleAdmin)
