from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from product.serializers import *
from utils.responses import response_schema

create_product_schema = extend_schema(
    summary="Create product",
    request=ProductCreateSerializer,
    responses=response_schema
)

update_product_schema = extend_schema(
    summary="Update Product",
    request=ProductUpdateSerializer,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='Product ID', required=True, type=OpenApiTypes.INT),
    ]
)

delete_product_schema = extend_schema(
    summary="Delete product",
    request=None,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='Product ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_products_schema = extend_schema(
    request=None,
    responses=ProductGetSerializer,
    summary="Get products",
    parameters=[
        OpenApiParameter(name='status', description="Choice 'sold' or 'on_sold'",
                         required=True, type=OpenApiTypes.STR, enum=['sold', 'on_sale']),
        OpenApiParameter(name='search', description='name or imei', required=False, type=OpenApiTypes.STR),
    ]
)

get_product_schema = extend_schema(
    summary="Get product",
    responses=ProductGetSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Product ID', required=True, type=OpenApiTypes.INT),
    ]
)

export_products_to_excel_schema = extend_schema(
    summary="Export products that unsold",
    responses=None
)
