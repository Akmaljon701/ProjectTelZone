from django.urls import path
from client.views import *


urlpatterns = [
    path('create/', create_client, name='create_client'),
    path('all/', get_clients, name='get_clients'),
    path('', get_client, name='get_client'),
    # path('delete/', delete_client, name='delete_client'),
]
