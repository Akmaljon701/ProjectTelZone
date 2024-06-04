from django.urls import path
from sale.views import *

urlpatterns = [
    path('create/', create_sale, name='create_sale'),
    path('update/', update_sale, name='update_sale'),
    path('all/', get_sales, name='get_sales'),
    path('', get_sale, name='get_sale'),
]
