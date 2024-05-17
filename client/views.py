from django.db.models import Q
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view
from client.models import Client
from client.serializers import ClientCreateSerializer, ClientUpdateSerializer, ClientGetSerializer
from rest_framework.response import Response
from utils.pagination import paginate
from utils.responses import success


@extend_schema(summary="Client create", request=ClientCreateSerializer, responses=None)
@api_view(['POST'])
def create_client(request):
    serializer = ClientCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@extend_schema(
    summary="Update Client",
    request=ClientUpdateSerializer,
    responses=None,
    parameters=[
        OpenApiParameter(name='pk', description='Client ID', required=True, type=OpenApiTypes.INT),
    ]
)
@api_view(['PUT'])
def update_client(request):
    pk = request.query_params.get('pk')
    client = Client.objects.get(id=pk)
    serializer = ClientUpdateSerializer(client, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@extend_schema(
    summary="Get clients",
    request=None,
    responses=ClientGetSerializer,
    parameters=[
        OpenApiParameter(name='search', description='FIO or phone', required=False, type=OpenApiTypes.STR),
    ]
)
@api_view(['GET'])
def get_clients(request):
    clients = Client.objects.all().order_by('FIO')
    search = request.query_params.get('search')
    if search: clients = clients.filter(Q(FIO__icontains=search) | Q(phone_number__icontains=search))
    return paginate(clients, ClientGetSerializer, request)


@extend_schema(
    summary="Get client",
    responses=ClientGetSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Client ID', required=True, type=OpenApiTypes.INT),
    ]
)
@api_view(['GET'])
def get_client(request):
    pk = request.query_params.get('pk')
    client = Client.objects.get(id=pk)
    serializer = ClientGetSerializer(client)
    return Response(serializer.data, status=200)

