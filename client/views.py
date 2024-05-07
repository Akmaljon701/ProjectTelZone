from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from client.models import Client
from client.serializers import ClientSerializer
from rest_framework.response import Response


@extend_schema(
    summary="Client create",
    request=ClientSerializer,
    responses={
        201: ClientSerializer
    },
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@extend_schema(
    summary="Get clients",
    responses=ClientSerializer(many=True)
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_clients(request):
    clients = Client.objects.all().order_by('FIO')
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data, status=200)


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

