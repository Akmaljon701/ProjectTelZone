from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter

from dashboard.serializers import ExpenseCreateSerializer, ExpenseUpdateSerializer, ExpenseGetSerializer
from utils.responses import response_schema

get_payment_results_schema = extend_schema(
    summary="Get payment results",
    responses=None,
    parameters=[
        OpenApiParameter(name='from_date', description='from_date', required=False, type=OpenApiTypes.DATE),
        OpenApiParameter(name='to_date', description='to_date', required=False, type=OpenApiTypes.DATE),
    ]
)

create_expense_schema = extend_schema(
    summary="Cerate Expense",
    request=ExpenseCreateSerializer,
    responses=response_schema
)

update_expense_schema = extend_schema(
    summary="Update Expense",
    request=ExpenseUpdateSerializer,
    responses=response_schema,
    parameters=[
        OpenApiParameter(name='pk', description='Expense ID', required=True, type=OpenApiTypes.INT),
    ]
)

get_expenses_schema = extend_schema(
    request=None,
    responses=ExpenseGetSerializer,
    summary="Get expenses",
    parameters=[
        OpenApiParameter(name='search', description='type', required=False, type=OpenApiTypes.STR)
    ]
)

get_expense_schema = extend_schema(
    summary="Get expense",
    responses=ExpenseGetSerializer,
    parameters=[
        OpenApiParameter(name='pk', description='Expense ID', required=True, type=OpenApiTypes.INT),
    ]
)
