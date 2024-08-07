from django.db import transaction
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.schemas import *
from product.serializers import ProductCreateSerializer, ProductUpdateSerializer, ProductGetSerializer
from utils.pagination import paginate, CustomOffSetPagination
from utils.permissions import check_allowed
from utils.responses import success


@create_product_schema
@api_view(['POST'])
@check_allowed('product_can_create')
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
@check_allowed('product_can_update')
def update_product(request):
    pk = request.query_params.get('pk')
    product = Product.objects.get(id=pk)
    if product.status == 'sold':
        return Response({'detail': 'The sold product cannot be changed!'}, 400)
    serializer = ProductUpdateSerializer(product, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    purchase_price = serializer.validated_data['purchase_price']
    percent = serializer.validated_data['percent']
    price = serializer.validated_data['price']
    if percent == 0:
        if purchase_price >= price:
            return Response({'detail': 'The price cannot be less than or equal to the purchased price!'}, status=422)
        difference = price - purchase_price
        percent = (difference * 100) / purchase_price
        serializer.save(percent=percent)
        return success
    elif price == 0:
        if percent <= 0:
            return Response("Price must not be equal to or less than 0!", status=422)
        price = purchase_price + ((purchase_price * percent) / 100)
        serializer.save(price=price)
        return success
    else:
        return Response({'detail': 'Unexpected error! (Note: price or percent must be 0)'}, status=400)


@delete_product_schema
@api_view(['DELETE'])
@check_allowed('product_can_delete')
@transaction.atomic
def delete_product(request):
    pk = request.query_params.get('pk')
    product = Product.objects.get(id=pk)
    if product.status == 'sold':
        return Response({'detail': 'The sold product cannot be deleted!'}, 400)
    product.delete()
    return success


@get_products_schema
@api_view(['GET'])
@check_allowed('product_can_view')
def get_products(request):
    status = request.query_params.get('status')
    search = request.query_params.get('search')
    products = Product.objects.filter(status=status).all().order_by('-id')
    if search: products = products.filter(Q(name__icontains=search) | Q(imei__icontains=search))

    paginator = CustomOffSetPagination()
    paginated_order = paginator.paginate_queryset(products, request)
    serializer = ProductGetSerializer(paginated_order, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@get_on_sale_products_for_select_schema
@api_view(['GET'])
@check_allowed('product_can_view')
def get_on_sale_products_for_select(request):
    search = request.query_params.get('search')
    if search:
        products = Product.objects.filter(Q(name__icontains=search) | Q(imei__icontains=search))
    else:
        products = Product.objects.filter(status='on_sale').all().order_by('-id')[:50]
    serializer = ProductGetSerializer(products, many=True, context={'request': request})
    return Response(serializer.data, 200)


@get_product_schema
@api_view(['GET'])
@check_allowed('product_can_view')
def get_product(request):
    pk = request.query_params.get('pk')
    client = Product.objects.get(id=pk)
    serializer = ProductGetSerializer(client, context={'request': request})
    return Response(serializer.data, status=200)
