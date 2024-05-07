from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from product.models import Product
from product.serializers import ProductSerializer


@extend_schema(
    summary="Client product",
    request=ProductSerializer,
    responses={
        201: ProductSerializer
    },
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def create_product(request):
    """
    Agar percent yozilsa price ga shu percent ga qarab purchase_price ustiga qo'shiladi,
    price yozilsa necha percent qoshilgani backend tomondan hisoblanadi,
    shunichun Frontda price yozilsa price input chiqmasin, price yozilsa aksincha bo'lsin
    """
    serializer = ProductSerializer(data=request.data)
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
        return Response(serializer.data, status=201)
    elif price == 0:
        if percent <= 0:
            return Response("Price must not be equal to or less than 0!", status=422)
        price = purchase_price + ((purchase_price * percent) / 100)
        serializer.save(status='on_sale', price=price)
        return Response(serializer.data, status=201)
    else:
        return Response({'detail': 'Unexpected error! (Note: price or percent must be 0)'}, status=400)


@extend_schema(
    summary="Get products",
    responses=ProductSerializer(many=True),
    parameters=[
        OpenApiParameter(name='status', description="Choice 'sold' or 'on_sold'",
                         required=True, type=OpenApiTypes.STR, enum=['sold', 'on_sale']),
    ]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_products(request):
    status = request.query_params.get('status')
    clients = Product.objects.filter(status=status).order_by('-id').all()
    serializer = ProductSerializer(clients, many=True)
    return Response(serializer.data, status=200)


@extend_schema(
    summary="Get product",
    responses=ProductSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Product ID', required=True, type=OpenApiTypes.INT),
    ]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_product(request):
    pk = request.query_params.get('pk')
    client = Product.objects.get(id=pk)
    serializer = ProductSerializer(client)
    return Response(serializer.data, status=200)

