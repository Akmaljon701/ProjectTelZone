from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import CustomUser, CustomUserPermission
from user.schemas import create_user_schema, get_current_user_schema, update_user_schema, \
    get_users_schema, get_user_schema, update_current_user_schema, update_user_permissions_schema
from user.serializers import CustomUserSerializer, CustomUserGetSerializer, CurrentUserUpdateSerializer, \
    CurrentUserGetSerializer, CustomUserPermissionSerializer
from utils.pagination import paginate
from utils.permissions import check_allowed, allowed_only_admin
from utils.responses import success
from django.db import transaction


@create_user_schema
@api_view(['POST'])
@check_allowed('user_can_create')
@transaction.atomic
def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    if user.role == 'worker':
        CustomUserPermission.objects.create(user=user)
    return success


@update_user_schema
@api_view(['PUT'])
@check_allowed('user_can_update')
def update_user(request):
    pk = request.query_params.get('pk')
    user = CustomUser.objects.get(id=pk)
    serializer = CustomUserSerializer(user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@get_users_schema
@api_view(['GET'])
@check_allowed('user_can_view')
def get_users(request):
    search = request.query_params.get('search')
    enum = request.query_params.get('enum')
    users = CustomUser.objects.select_related('permission_fields').all().order_by('username')
    if search: users = users.filter(Q(username__icontains=search) |
                                    Q(first_name__icontains=search) |
                                    Q(last_name__icontains=search))
    if enum: users = users.filter(role=enum)
    return paginate(users, CustomUserGetSerializer, request)


@get_user_schema
@api_view(['GET'])
@check_allowed('user_can_view')
def get_user(request):
    pk = request.query_params.get('pk')
    user = CustomUser.objects.select_related('permission_fields').get(id=pk)
    serializer = CustomUserGetSerializer(user)
    return Response(serializer.data, status=200)


@get_current_user_schema
@api_view(['GET'])
def get_current_user(request):
    serializer = CurrentUserGetSerializer(request.user)
    return Response(serializer.data, status=200)


@update_current_user_schema
@api_view(['PUT'])
def update_current_user(request):
    serializer = CurrentUserUpdateSerializer(request.user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@update_user_permissions_schema
@api_view(['PUT'])
@allowed_only_admin()
def update_user_permissions(request):
    pk = request.query_params.get('pk')
    user_permissions = CustomUserPermission.objects.get(user=pk)
    serializer = CustomUserPermissionSerializer(user_permissions, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success
