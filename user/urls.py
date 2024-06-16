from django.urls import path
from user.views import *


urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('update/', update_user, name='update_user'),
    path('all/', get_users, name='get_users'),
    path('', get_user, name='get_user'),
    path('current/', get_current_user, name='get_current_user'),
    path('custom/update/', update_custom_user, name='update_custom_user'),
]
