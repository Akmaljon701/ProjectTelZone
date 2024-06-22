from django.contrib import admin
from dashboard.models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'price', 'date')
    list_display_links = ('type', 'price', 'date')
    search_fields = ('price', 'date')


admin.site.register(Expense, ExpenseAdmin)
