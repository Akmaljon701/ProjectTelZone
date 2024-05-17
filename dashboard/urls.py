from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('payment/results/', get_payment_results, name='get_payment_results'),
]
