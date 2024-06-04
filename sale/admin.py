from django.contrib import admin
from sale.forms import SaleAdminForm, CreditBaseAdminForm
from sale.models import Sale, CreditBase


class CreditBaseAdmin(admin.ModelAdmin):
    form = CreditBaseAdminForm
    list_display = ('id', 'nazvanie')
    list_display_links = ('id', 'nazvanie')
    search_fields = ('name',)

    def nazvanie(self, obj):
        return obj.name

    nazvanie.short_description = "Название"


class SaleAdmin(admin.ModelAdmin):
    form = SaleAdminForm
    list_display = ('id', 'produkt', 'klient', 'baza', 'prodannaya_tsena', 'data')
    list_display_links = ('produkt', 'klient', 'baza', 'prodannaya_tsena', 'data')
    search_fields = ('product__name', 'client__FIO', 'client__phone_number', 'sold_price', 'date')
    list_filter = ['date']
    autocomplete_fields = ['product', 'client', 'credit_base']

    def produkt(self, obj):
        return ", ".join([product.name for product in obj.product.all()])

    def klient(self, obj):
        return obj.client

    def baza(self, obj):
        return ", ".join([credit_base.name for credit_base in obj.credit_base.all()])

    def prodannaya_tsena(self, obj):
        return obj.sold_price

    def data(self, obj):
        return obj.date

    produkt.short_description = "Продукт"
    klient.short_description = "Клиент"
    baza.short_description = 'Рассрочка База'
    prodannaya_tsena.short_description = 'Проданная цена'
    data.short_description = 'Дата'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            super().save_model(request, obj, form, change)
        if 'product' in form.cleaned_data:
            obj.product.set(form.cleaned_data['product'])
        if 'credit_base' in form.cleaned_data:
            obj.credit_base.set(form.cleaned_data['credit_base'])
        for product in obj.product.all():
            product.count -= 1
            if product.count == 0:
                product.status = 'sold'
            product.save()
        super().save_model(request, obj, form, change)


admin.site.register(Sale, SaleAdmin)
admin.site.register(CreditBase, CreditBaseAdmin)
