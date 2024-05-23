from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.schemas import *
from product.serializers import ProductCreateSerializer, ProductUpdateSerializer, ProductGetSerializer
from utils.pagination import paginate
from utils.responses import success


@create_product_schema
@api_view(['POST'])
def create_product(request):
    """
    Agar percent yozilsa price ga shu percent ga qarab purchase_price ustiga qo'shiladi,
    price yozilsa necha percent qoshilgani backend tomondan hisoblanadi,
    shunichun Frontda price yozilsa price input chiqmasin, price yozilsa aksincha bo'lsin
    """
    serializer = ProductCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    purchase_price = serializer.validated_data['purchase_price']
    percent = serializer.validated_data['percent']
    price = serializer.validated_data['price']
    if percent == 0:
        if purchase_price >= price:
            return Response({'detail': 'The price cannot be less than or equal to the purchased price!'}, status=422)
        difference = price - purchase_price
        percent = (difference * 100) / purchase_price
        serializer.save(status='on_sale', percent=percent)
        return success
    elif price == 0:
        if percent <= 0:
            return Response("Price must not be equal to or less than 0!", status=422)
        price = purchase_price + ((purchase_price * percent) / 100)
        serializer.save(status='on_sale', price=price)
        return success
    else:
        return Response({'detail': 'Unexpected error! (Note: price or percent must be 0)'}, status=400)


@update_product_schema
@api_view(['PUT'])
def update_product(request):
    pk = request.query_params.get('pk')
    product = Product.objects.get(id=pk)
    serializer = ProductUpdateSerializer(product, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@get_products_schema
@api_view(['GET'])
def get_products(request):
    status = request.query_params.get('status')
    search = request.query_params.get('search')
    clients = Product.objects.filter(status=status).all().order_by('-id')
    if search: clients = clients.filter(Q(name__icontains=search) | Q(imei__icontains=search))
    return paginate(clients, ProductGetSerializer, request)


@get_product_schema
@api_view(['GET'])
def get_product(request):
    pk = request.query_params.get('pk')
    client = Product.objects.get(id=pk)
    serializer = ProductGetSerializer(client)
    return Response(serializer.data, status=200)
