from django.db import transaction
from django.db.models import Q
from rest_framework.decorators import api_view
from client.schemas import *
from client.serializers import ClientCreateSerializer, ClientUpdateSerializer, ClientGetSerializer
from rest_framework.response import Response

from sale.models import Sale
from utils.pagination import paginate
from utils.permissions import check_allowed
from utils.responses import success


@create_client_schema
@api_view(['POST'])
@check_allowed('client_can_create')
def create_client(request):
    serializer = ClientCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@update_client_schema
@api_view(['PUT'])
@check_allowed('client_can_update')
def update_client(request):
    pk = request.query_params.get('pk')
    client = Client.objects.get(id=pk)
    serializer = ClientUpdateSerializer(client, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@delete_client_schema
@api_view(['DELETE'])
@check_allowed('client_can_delete')
@transaction.atomic
def delete_client(request):
    pk = request.query_params.get('pk')
    client = Client.objects.get(id=pk)
    sale = Sale.objects.filter(client=client)
    if sale:
        return Response('A transaction was made with this client. Failed to delete!', 400)
    client.delete()
    return success


@get_clients_schema
@api_view(['GET'])
@check_allowed('client_can_view')
def get_clients(request):
    clients = Client.objects.all().order_by('FIO')
    search = request.query_params.get('search')
    if search: clients = clients.filter(Q(FIO__icontains=search) | Q(phone_number__icontains=search))
    return paginate(clients, ClientGetSerializer, request)


@get_clients_for_select_schema
@api_view(['GET'])
@check_allowed('client_can_view')
def get_clients_for_select(request):
    clients = Client.objects.all().order_by('-id')
    search = request.query_params.get('search')
    if search: clients = clients.filter(Q(FIO__icontains=search) | Q(phone_number__icontains=search))
    serializer = ClientGetSerializer(clients, many=True)
    return Response(serializer.data, 200)


@get_client_schema
@api_view(['GET'])
@check_allowed('client_can_view')
def get_client(request):
    pk = request.query_params.get('pk')
    client = Client.objects.get(id=pk)
    serializer = ClientGetSerializer(client)
    return Response(serializer.data, status=200)

