from drf_spectacular.utils import extend_schema
from user.serializers import CustomUserSerializer
from utils.responses import response_schema

get_current_user_schema = extend_schema(
    summary="Get current user",
    responses=CustomUserSerializer
)

update_custom_user_schema = extend_schema(
    summary="Get current user",
    request=CustomUserSerializer,
    responses=response_schema
)
