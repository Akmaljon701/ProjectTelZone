from django.urls import path
from sale.views import *

urlpatterns = [
    path('product/', sell_product, name='sell_product'),
]
