from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from utils.responses import response_schema
from .serializers import *

create_client_schema = extend_schema(
    summary="Client create",
    request=ClientCreateSerializer,
    responses=response_schema
)

update_client_schema = extend_schema(
    summary="Update Client",
    request=ClientUpdateSerializer,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='Client ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_clients_schema = extend_schema(
    summary="Get clients",
    request=None,
    responses=ClientGetSerializer,
    parameters=[
        OpenApiParameter(name='search', description='FIO or phone', required=False, type=OpenApiTypes.STR),
    ]
)

get_client_schema = extend_schema(
    summary="Get client",
    responses=ClientGetSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Client ID', required=True, type=OpenApiTypes.INT),
    ]
)

