from django.urls import path
from user.views import *


urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('update/', update_user, name='update_user'),
    path('all/', get_users, name='get_users'),
    path('select/', get_users_for_select, name='get_users_for_select'),
    path('', get_user, name='get_user'),
    path('current/', get_current_user, name='get_current_user'),
    path('current/update/', update_current_user, name='update_custom_user'),
    path('update/permissions/', update_user_permissions, name='update_user_permissions'),
]
