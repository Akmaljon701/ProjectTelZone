from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from django.db.models import Sum, F, Q
from dashboard.models import Expense
from dashboard.serializers import ExpenseCreateSerializer, ExpenseUpdateSerializer, ExpenseGetSerializer
from product.models import Product
from sale.models import Sale
from dashboard.schemas import get_payment_results_schema, create_expense_schema, update_expense_schema, \
    get_expenses_schema, get_expense_schema
from sale.serializers import SaleGetSerializer
from utils.pagination import paginate
from utils.permissions import check_allowed
from utils.responses import success


@get_payment_results_schema
@api_view(['GET'])
@check_allowed('dashboard_can_view')
# @permission_classes([AllowAny])
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
        today = datetime.now().date()
        start_of_month = today.replace(day=1)
        text = f'{start_of_month} - {today}'

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
                     # 'expenses_data': ExpenseGetSerializer(expenses.all(), many=True).data,
                     'sales': total_sales,
                     # 'sales_data': SaleGetSerializer(sales.all(), many=True).data,
                     'warehouse': {
                         'purchase_price': total_purchase_price,
                         'price': total_price,
                     }}, status=200)


@create_expense_schema
@api_view(['POST'])
@check_allowed('expense_can_create')
def create_expense(request):
    serializer = ExpenseCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@update_expense_schema
@api_view(['PUT'])
@check_allowed('expense_can_update')
def update_expense(request):
    pk = request.query_params.get('pk')
    expense = Expense.objects.get(id=pk)
    serializer = ExpenseUpdateSerializer(expense, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return success


@get_expenses_schema
@api_view(['GET'])
@check_allowed('expense_can_view')
def get_expenses(request):
    expenses = Expense.objects.all().order_by('-id')
    return paginate(expenses, ExpenseGetSerializer, request)


@get_expense_schema
@api_view(['GET'])
@check_allowed('expense_can_view')
def get_expense(request):
    pk = request.query_params.get('pk')
    expense = Expense.objects.get(id=pk)
    serializer = ExpenseGetSerializer(expense)
    return Response(serializer.data, status=200)
