from django.contrib import admin
from product.forms import ProductAdminForm
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('id', 'name', 'purchase_price', 'percent', 'price', 'date', 'status')
    list_display_links = ('name', 'purchase_price', 'percent', 'price', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = ('name', 'price', 'date')
    ordering = ['name']


admin.site.register(Product, ProductAdmin)
