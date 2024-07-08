from django.urls import path
from client.views import *


urlpatterns = [
    path('create/', create_client, name='create_client'),
    path('update/', update_client, name='update_client'),
    path('delete/', delete_client, name='delete_client'),
    path('all/', get_clients, name='get_clients'),
    path('select/', get_clients_for_select, name='get_clients_for_select'),
    path('', get_client, name='get_client'),
]
