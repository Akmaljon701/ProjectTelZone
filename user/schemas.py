from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from user.serializers import CustomUserSerializer, CustomUserGetSerializer, CurrentUserUpdateSerializer, \
    CurrentUserGetSerializer, CustomUserPermissionSerializer
from utils.responses import response_schema

create_user_schema = extend_schema(
    summary="User create",
    request=CustomUserSerializer,
    responses=response_schema
)

update_user_schema = extend_schema(
    summary="User update",
    request=CustomUserSerializer(many=True),
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='User ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_users_schema = extend_schema(
    summary="Get users",
    request=None,
    responses=CustomUserGetSerializer,
    parameters=[
        OpenApiParameter(name='search', description='username, first_name, last_name',
                         required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name='enum', description='Choice one option', required=True,
                         type=OpenApiTypes.STR, enum=['admin', 'worker'])
    ]
)

get_users_for_select_schema = extend_schema(
    summary="Get users",
    request=None,
    responses=CustomUserGetSerializer(many=True),
    parameters=[
        OpenApiParameter(name='search', description='username', required=False, type=OpenApiTypes.STR),
    ]
)

get_user_schema = extend_schema(
    summary="Get user",
    responses=CustomUserGetSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='User ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_current_user_schema = extend_schema(
    summary="Get current user",
    responses=CurrentUserGetSerializer
)

update_current_user_schema = extend_schema(
    summary="update current user",
    request=CurrentUserUpdateSerializer,
    responses=response_schema
)

update_user_permissions_schema = extend_schema(
    summary="User permissions update",
    request=CustomUserPermissionSerializer,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='User ID', required=True, type=OpenApiTypes.INT),
    ]
)
