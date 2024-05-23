from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from sale.serializers import *
from utils.responses import response_schema

sell_product_schema = extend_schema(
    summary="Sell product",
    request=SaleCreateSerializer,
    responses=response_schema
)

update_sale_schema = extend_schema(
    summary="Update sale",
    request=SaleUpdateSerializer,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='Sale ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_sales_schema = extend_schema(
    summary="Get sales",
    responses=SaleGetSerializer(many=True)
)

get_sale_schema = extend_schema(
    summary="Get sale",
    responses=SaleGetSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Sale ID', required=True, type=OpenApiTypes.INT),
    ]
)
