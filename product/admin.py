from django.contrib import admin
from product.forms import ProductAdminForm
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('id', 'name', 'purchase_price', 'percent', 'price', 'count', 'date', 'status')
    list_display_links = ('name', 'purchase_price', 'percent', 'price', 'count', 'date', 'status')
    list_filter = ('date',)
    search_fields = ('name', 'price', 'date')
    ordering = ['name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status='on_sale')


admin.site.register(Product, ProductAdmin)
