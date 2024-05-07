from django.contrib import admin
from product.models import Product, Expense


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'percent', 'price', 'date', 'status')
    list_display_links = ('name', 'purchase_price', 'percent', 'price', 'date')
    list_filter = ('date', 'status')
    search_fields = ('name', 'price', 'date')
    ordering = ['name']


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'price', 'date')
    list_display_links = ('type', 'price', 'date')
    search_fields = ('price', 'date')


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Product, ProductAdmin)
