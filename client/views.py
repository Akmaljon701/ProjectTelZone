from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from client.models import Client
from client.serializers import ClientSerializer
from rest_framework.response import Response

from utils.pagination import paginate
from utils.responses import success


@extend_schema(summary="Client create", request=ClientSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@extend_schema(
    summary="Get clients",
    parameters=[
        OpenApiParameter(name='FIO', description='FIO', required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name='phone_number', description='phone_number', required=False, type=OpenApiTypes.STR),
    ]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_clients(request):
    clients = Client.objects.all().order_by('FIO')
    fio = request.query_params.get('FIO')
    phone_number = request.query_params.get('phone_number')
    if fio: clients = clients.filter(FIO__icontains=fio)
    elif phone_number: clients = clients.filter(phone_number__icontains=phone_number)
    return paginate(clients, ClientSerializer, request)


@extend_schema(
    summary="Get client",
    responses=ClientSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Client ID', required=True, type=OpenApiTypes.INT),
    ]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_client(request):
    pk = request.query_params.get('pk')
    client = Client.objects.get(id=pk)
    serializer = ClientSerializer(client)
    return Response(serializer.data, status=200)


# @extend_schema(
#     summary="Delete client",
#     parameters=[
#         OpenApiParameter(name='pk', description='Client ID', required=True, type=OpenApiTypes.INT),
#     ]
# )
# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# @renderer_classes([JSONRenderer])
# def delete_client(request):
#     pk = request.query_params.get('pk')
#     client = Client.objects.get(id=pk)
#     client.delete()
#     return Response(status=204)

