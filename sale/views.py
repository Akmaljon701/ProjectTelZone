from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from client.models import Client
from product.models import Product
from sale.models import Sale
from sale.serializers import SellProductSerializer
from utils.pagination import paginate
from utils.responses import success


@extend_schema(summary="Sell product", request=SellProductSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def sell_product(request):
    serializer = SellProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    product = Product.objects.get(id=serializer.validated_data['product'].id, status='on_sale', count__gt=0)
    serializer.save(product=product, client=serializer.validated_data['client'])
    product.count -= 1
    if product.count == 0:
        product.status = 'sold'
    product.save()
    return success
