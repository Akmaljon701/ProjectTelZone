from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product
from sale.schemas import *
from sale.serializers import SaleGetSerializer, SaleCreateSerializer, SaleUpdateSerializer
from utils.pagination import paginate
from utils.responses import success


@sell_product_schema
@api_view(['POST'])
def sell_product(request):
    serializer = SaleCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    product = Product.objects.get(id=serializer.validated_data['product'].id, status='on_sale', count__gt=0)
    serializer.save(product=product, client=serializer.validated_data['client'])
    product.count -= 1
    if product.count == 0:
        product.status = 'sold'
    product.save()
    return success


@update_sale_schema
@api_view(['PUT'])
def update_sale(request):
    pk = request.query_params.get('pk')
    sale = Sale.objects.get(id=pk)
    serializer = SaleUpdateSerializer(sale, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@get_sales_schema
@api_view(['GET'])
def get_sales(request):
    sales = Sale.objects.select_related('client', 'product').order_by('-id').all()
    return paginate(sales, SaleGetSerializer, request)


@get_sale_schema
@api_view(['GET'])
def get_sale(request):
    pk = request.query_params.get('pk')
    sale = Sale.objects.select_related('client', 'product').get(id=pk)
    serializer = SaleGetSerializer(sale)
    return Response(serializer.data, status=200)
