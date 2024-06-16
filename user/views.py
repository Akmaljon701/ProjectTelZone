from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import CustomUser
from user.schemas import create_user_schema, get_current_user_schema, update_custom_user_schema, update_user_schema, \
    get_users_schema, get_user_schema
from user.serializers import CustomUserSerializer
from utils.pagination import paginate
from utils.responses import success


@create_user_schema
@api_view(['POST'])
def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@update_user_schema
@api_view(['PUT'])
def update_user(request):
    pk = request.query_params.get('pk')
    user = CustomUser.objects.get(id=pk)
    serializer = CustomUserSerializer(user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@get_users_schema
@api_view(['GET'])
def get_users(request):
    search = request.query_params.get('search')
    enum = request.query_params.get('enum')
    users = CustomUser.objects.all().order_by('username')
    if search: users = users.filter(Q(username__icontains=search) |
                                    Q(first_name__icontains=search) |
                                    Q(last_name__icontains=search))
    if enum: users = users.filter(role=enum)
    return paginate(users, CustomUserSerializer, request)


@get_user_schema
@api_view(['GET'])
def get_user(request):
    pk = request.query_params.get('pk')
    user = CustomUser.objects.get(id=pk)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data, status=200)


@get_current_user_schema
@api_view(['GET'])
def get_current_user(request):
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data, status=200)


@update_custom_user_schema
@api_view(['PUT'])
def update_custom_user(request):
    serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success
