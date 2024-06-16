from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from user.serializers import CustomUserSerializer
from utils.responses import response_schema

create_user_schema = extend_schema(
    summary="User create",
    request=CustomUserSerializer,
    responses=response_schema
)

update_user_schema = extend_schema(
    summary="User update",
    request=CustomUserSerializer,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='User ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_users_schema = extend_schema(
    summary="Get users",
    request=None,
    responses=CustomUserSerializer,
    parameters=[
        OpenApiParameter(name='search', description='username, first_name, last_name',
                         required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name='enum', description='Choice one option', required=True,
                         type=OpenApiTypes.STR, enum=['admin', 'worker'])
    ]
)

get_user_schema = extend_schema(
    summary="Get user",
    responses=CustomUserSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='User ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_current_user_schema = extend_schema(
    summary="Get current user",
    responses=CustomUserSerializer
)

update_custom_user_schema = extend_schema(
    summary="update current user",
    request=CustomUserSerializer,
    responses=response_schema
)
