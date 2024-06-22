from django.contrib import admin
from sale.models import Sale, CreditBase


class CreditBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_products', 'client', 'get_credit_bases', 'sold_price', 'date')
    list_display_links = ('get_products', 'client', 'get_credit_bases', 'sold_price', 'date')
    search_fields = ('product__name', 'client__FIO', 'client__phone_number', 'sold_price', 'date')
    list_filter = ['date']
    autocomplete_fields = ['product', 'client', 'credit_base']

    def get_products(self, obj):
        return ", ".join([product.name for product in obj.product.all()])

    def get_credit_bases(self, obj):
        return ", ".join([credit_base.name for credit_base in obj.credit_base.all()])

    get_products.short_description = 'Продукти'
    get_credit_bases.short_description = 'Рассрочка Бази'

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
