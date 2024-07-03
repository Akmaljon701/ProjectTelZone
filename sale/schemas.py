from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from sale.serializers import SaleGetSerializer, SaleCreateSerializer, SaleUpdateSerializer, CreditBaseCreateSerializer, \
    CreditBaseUpdateSerializer, CreditBaseGetSerializer, SalesGetSerializer
from utils.responses import response_schema

create_sale_schema = extend_schema(
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

delete_sale_schema = extend_schema(
    summary="Delete sale",
    request=None,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='Sale ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_sales_schema = extend_schema(
    summary="Get sales",
    responses=SalesGetSerializer(many=True),
    parameters=[
        OpenApiParameter(name='search', description='client fio, client phone number, product name, product imei',
                         required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name='from_date', description='from_date', required=False, type=OpenApiTypes.DATE),
        OpenApiParameter(name='to_date', description='to_date', required=False, type=OpenApiTypes.DATE),
        OpenApiParameter(name='user', description='User ID', required=False, type=OpenApiTypes.INT),
    ]
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
    request=CreditBaseUpdateSerializer,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='Credit Base ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_credit_bases_schema = extend_schema(
    summary="Get Credit Bases",
    responses=CreditBaseGetSerializer(many=True),
    parameters=[
        OpenApiParameter(name='search', description='name', required=False, type=OpenApiTypes.STR),
    ]
)

get_credit_base_schema = extend_schema(
    summary="Get Credit Base",
    responses=CreditBaseGetSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Credit Base ID', required=True, type=OpenApiTypes.INT),
    ]
)

export_sales_to_excel_schema = extend_schema(
    summary="Export sales",
    responses=None,
    parameters=[
        OpenApiParameter(name='pk', description='User ID', required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name='from_date', description='from_date', required=True, type=OpenApiTypes.DATE),
        OpenApiParameter(name='to_date', description='to_date', required=True, type=OpenApiTypes.DATE),
    ]
)
