from django.urls import path
from sale.export_to_xls import export_sales_to_excel
from sale.views import *

urlpatterns = [
    path('create/', create_sale, name='create_sale'),
    path('update/', update_sale, name='update_sale'),
    path('delete/', delete_sale, name='delete_sale'),
    path('all/', get_sales, name='get_sales'),
    path('', get_sale, name='get_sale'),
    # path('export-sales/', export_sales_to_excel, name='export_sales_to_excel'),
]
