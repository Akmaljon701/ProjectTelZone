from django.db.models import Q
from rest_framework.decorators import api_view
from client.schemas import *
from client.serializers import ClientCreateSerializer, ClientUpdateSerializer, ClientGetSerializer
from rest_framework.response import Response
from utils.pagination import paginate
from utils.responses import success


@create_client_schema
@api_view(['POST'])
def create_client(request):
    serializer = ClientCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@update_client_schema
@api_view(['PUT'])
def update_client(request):
    pk = request.query_params.get('pk')
    client = Client.objects.get(id=pk)
    serializer = ClientUpdateSerializer(client, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@get_clients_schema
@api_view(['GET'])
def get_clients(request):
    clients = Client.objects.all().order_by('FIO')
    search = request.query_params.get('search')
    if search: clients = clients.filter(Q(FIO__icontains=search) | Q(phone_number__icontains=search))
    return paginate(clients, ClientGetSerializer, request)


@get_client_schema
@api_view(['GET'])
def get_client(request):
    pk = request.query_params.get('pk')
    client = Client.objects.get(id=pk)
    serializer = ClientGetSerializer(client)
    return Response(serializer.data, status=200)

