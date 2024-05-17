from django.contrib import admin
from product.forms import ProductAdminForm
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('id', 'nazvanie', 'tsena_pokupki', 'protsent', 'tsena', 'sht', 'data', 'status_ru')
    list_display_links = ('nazvanie', 'tsena_pokupki', 'protsent', 'tsena', 'sht', 'data', 'status_ru')
    list_filter = ('date',)
    search_fields = ('name', 'price', 'date')
    ordering = ['name']

    def nazvanie(self, obj):
        return obj.name

    def tsena_pokupki(self, obj):
        return obj.purchase_price

    def protsent(self, obj):
        return obj.percent

    def tsena(self, obj):
        return obj.price

    def sht(self, obj):
        return obj.count

    def data(self, obj):
        return obj.date

    def status_ru(self, obj):
        return obj.status

    nazvanie.short_description = 'Название'
    tsena_pokupki.short_description = 'Цена покупки'
    protsent.short_description = 'Процент'
    tsena.short_description = 'Цена'
    sht.short_description = 'Шт'
    data.short_description = 'Дата'
    status_ru.short_description = 'Статус'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status='on_sale')


admin.site.register(Product, ProductAdmin)
