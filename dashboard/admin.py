from django.contrib import admin
from dashboard.models import Expense
from dashboard.forms import ExpenseAdminForm


class ExpenseAdmin(admin.ModelAdmin):
    form = ExpenseAdminForm
    list_display = ('id', 'tip', 'tsena', 'data')
    list_display_links = ('tip', 'tsena', 'data')
    search_fields = ('price', 'date')

    def tip(self, obj):
        return obj.type

    def tsena(self, obj):
        return obj.price

    def data(self, obj):
        return obj.date

    tip.short_description = 'Тип'
    tsena.short_description = 'Цена'
    data.short_description = 'Дата'


admin.site.register(Expense, ExpenseAdmin)
