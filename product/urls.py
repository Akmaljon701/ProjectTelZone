from django.urls import path

from product.export_to_xls import export_products_to_excel
from product.views import *

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('update/', update_product, name='update_product'),
    path('delete/', delete_product, name='delete_product'),
    path('all/', get_products, name='get_products'),
    path('select/', get_on_sale_products_for_select, name='get_on_sale_products_for_select'),
    path('', get_product, name='get_product'),
    path('export/', export_products_to_excel, name='export_products_to_excel'),
]
