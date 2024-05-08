from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from client.models import Client
from product.models import Product
from sale.models import Sale
from sale.serializers import SaleSerializer, CreateAndUpdateSaleSerializer
from utils.pagination import paginate
from utils.responses import success


@extend_schema(summary="Sell product", request=CreateAndUpdateSaleSerializer, responses=None)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def sell_product(request):
    serializer = CreateAndUpdateSaleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    product = Product.objects.get(id=serializer.validated_data['product'].id, status='on_sale', count__gt=0)
    serializer.save(product=product, client=serializer.validated_data['client'])
    product.count -= 1
    if product.count == 0:
        product.status = 'sold'
    product.save()
    return success


@extend_schema(
    summary="Update sale",
    request=CreateAndUpdateSaleSerializer,
    responses=None,
    parameters=[
        OpenApiParameter(name='pk', description='Sale ID', required=True, type=OpenApiTypes.INT),
    ]
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def update_sale(request):
    pk = request.query_params.get('pk')
    sale = Sale.objects.get(id=pk)
    serializer = CreateAndUpdateSaleSerializer(sale, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@extend_schema(summary="Get sales", responses=SaleSerializer(many=True))
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_sales(request):
    sales = Sale.objects.order_by('-id').all()
    return paginate(sales, SaleSerializer, request)


@extend_schema(
    summary="Get sale",
    responses=SaleSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Sale ID', required=True, type=OpenApiTypes.INT),
    ]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_sale(request):
    pk = request.query_params.get('pk')
    sale = Sale.objects.get(id=pk)
    serializer = SaleSerializer(sale)
    return Response(serializer.data, status=200)
