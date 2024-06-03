from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from sale.serializers import SaleGetSerializer, SaleCreateSerializer, SaleUpdateSerializer, CreditBaseCreateSerializer, \
    UpdateBaseCreateSerializer, GetBaseCreateSerializer
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

create_credit_base_schema = extend_schema(
    summary="Create Credit Base",
    request=CreditBaseCreateSerializer,
    responses=response_schema
)

update_credit_base_schema = extend_schema(
    summary="Update Credit Base",
    request=UpdateBaseCreateSerializer,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='Credit Base ID', required=True, type=OpenApiTypes.INT),
    ]
)


get_credit_bases_schema = extend_schema(
    summary="Get Credit Bases",
    responses=GetBaseCreateSerializer(many=True)
)

get_credit_base_schema = extend_schema(
    summary="Get Credit Base",
    responses=GetBaseCreateSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Credit Base ID', required=True, type=OpenApiTypes.INT),
    ]
)
