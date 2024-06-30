from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sale.models import Sale, CreditBase
from sale.schemas import update_sale_schema, get_sales_schema, get_sale_schema, \
    create_credit_base_schema, update_credit_base_schema, get_credit_bases_schema, get_credit_base_schema, \
    create_sale_schema
from sale.serializers import SaleGetSerializer, SaleUpdateSerializer, CreditBaseCreateSerializer, SaleCreateSerializer, \
    CreditBaseUpdateSerializer, CreditBaseGetSerializer, SalesGetSerializer
from utils.pagination import paginate
from utils.permissions import check_allowed
from utils.responses import success


@create_sale_schema
@api_view(['POST'])
@check_allowed('sale_can_create')
def create_sale(request):
    serializer = SaleCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    sale = serializer.save(sold_user=request.user)
    for product in sale.product.all():
        product.count -= 1
        if product.count == 0:
            product.status = 'sold'
        product.save()
    return success


@update_sale_schema
@api_view(['PUT'])
@check_allowed('sale_can_update')
def update_sale(request):
    pk = request.query_params.get('pk')
    sale = Sale.objects.get(id=pk)
    serializer = SaleUpdateSerializer(sale, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@get_sales_schema
@api_view(['GET'])
@check_allowed('sale_can_view')
def get_sales(request):
    search = request.query_params.get('search')
    sales = Sale.objects.select_related('client').order_by('-id').all().prefetch_related('product', 'credit_base')
    if search: sales = sales.filter(Q(client__FIO__icontains=search) | Q(client__phone_number__icontains=search))
    return paginate(sales, SalesGetSerializer, request)


@get_sale_schema
@api_view(['GET'])
@check_allowed('sale_can_view')
def get_sale(request):
    pk = request.query_params.get('pk')
    sale = Sale.objects.select_related('client').prefetch_related('product', 'credit_base').get(id=pk)
    serializer = SaleGetSerializer(sale)
    return Response(serializer.data, status=200)


@create_credit_base_schema
@api_view(['POST'])
@check_allowed('credit_base_can_create')
def create_credit_base(request):
    serializer = CreditBaseCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@update_credit_base_schema
@api_view(['PUT'])
@check_allowed('credit_base_can_update')
def update_credit_base(request):
    pk = request.query_params.get('pk')
    credit_base = CreditBase.objects.get(id=pk)
    serializer = CreditBaseUpdateSerializer(credit_base, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@get_credit_bases_schema
@api_view(['GET'])
@check_allowed('credit_base_can_view')
def get_credit_bases(request):
    search = request.query_params.get('search')
    credit_bases = CreditBase.objects.order_by('-id').all()
    if search:
        credit_bases = credit_bases.filter(Q(name__icontains=search))
    return paginate(credit_bases, CreditBaseGetSerializer, request)


@get_credit_base_schema
@api_view(['GET'])
@check_allowed('credit_base_can_view')
def get_credit_base(request):
    pk = request.query_params.get('pk')
    credit_base = CreditBase.objects.get(id=pk)
    serializer = CreditBaseGetSerializer(credit_base)
    return Response(serializer.data, status=200)
