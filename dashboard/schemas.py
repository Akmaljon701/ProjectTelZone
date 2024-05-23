from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter

get_payment_results_schema = extend_schema(
    summary="Get payment results",
    responses=None,
    parameters=[
        OpenApiParameter(name='from_date', description='from_date', required=False, type=OpenApiTypes.DATE),
        OpenApiParameter(name='to_date', description='to_date', required=False, type=OpenApiTypes.DATE),
    ]
)
