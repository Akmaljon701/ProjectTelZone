from datetime import datetime
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from django.db.models import Sum, F
from dashboard.models import Expense
from product.models import Product
from sale.models import Sale


@extend_schema(
    summary="Get payment results",
    responses=None,
    parameters=[
        OpenApiParameter(name='from_date', description='from_date', required=False, type=OpenApiTypes.DATE),
        OpenApiParameter(name='to_date', description='to_date', required=False, type=OpenApiTypes.DATE),
    ]
)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_payment_results(request):
    from_date = request.query_params.get('from_date')
    to_date = request.query_params.get('to_date')
    if from_date and to_date:
        try:
            from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
            to_date = datetime.strptime(to_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'detail': 'from_date and to_date date format is wrong!'}, status=422)

        if from_date > to_date:
            return Response({'detail': 'from_date must be less than to_date!'}, status=422)

        text = f"{from_date} - {to_date}"
        expenses = Expense.objects.filter(date__range=(from_date, to_date))
        sales = Sale.objects.filter(date__range=(from_date, to_date))
    else:
        text = "This month's data"
        today = datetime.now().date()
        start_of_month = today.replace(day=1)

        expenses = Expense.objects.filter(date__range=(start_of_month, today))
        sales = Sale.objects.filter(date__range=(start_of_month, today))

    total_expenses = expenses.aggregate(total_price=Sum('price'))['total_price']
    total_sales = sales.aggregate(total_price=Sum('sold_price'))['total_price']

    remaining_products = Product.objects.filter(status='on_sale').all()
    total_purchase_price = remaining_products.aggregate(
        total_price=Sum(F('count') * F('purchase_price'))
    )['total_price']
    total_price = remaining_products.aggregate(
        total_price=Sum(F('count') * F('price'))
    )['total_price']

    return Response({'text': text,
                     'expenses': total_expenses,
                     'sales': total_sales,
                     'warehouse': {
                         'purchase_price': total_purchase_price,
                         'price': total_price,
                     }}, status=200)


