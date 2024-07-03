from datetime import datetime
import pandas as pd
from django.http import HttpResponse
from openpyxl.utils import get_column_letter
from rest_framework.decorators import api_view
from sale.models import Sale
from sale.schemas import export_sales_to_excel_schema
from utils.permissions import allowed_only_admin


@export_sales_to_excel_schema
@api_view(['GET'])
@allowed_only_admin()
def export_sales_to_excel(request):
    user = request.query_params.get('user')
    from_date = request.query_params.get('from_date')
    to_date = request.query_params.get('to_date')

    try:
        from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
        to_date = datetime.strptime(to_date, '%Y-%m-%d').date()
    except ValueError:
        return HttpResponse({'detail': 'from_date and to_date date format is wrong!'}, status=422)

    if from_date > to_date:
        return HttpResponse({'detail': 'from_date must be less than to_date!'}, status=422)

    if user:
        sales = Sale.objects.filter(
            sold_user=user,
            date__range=[from_date, to_date]
        ).select_related('client', 'sold_user').prefetch_related('product', 'credit_base')
    else:
        sales = Sale.objects.filter(
            date__range=[from_date, to_date]
        ).select_related('client', 'sold_user').prefetch_related('product', 'credit_base')

    sales_data = []
    total_sold_price = 0  # Initialize total sold price

    for sale in sales:
        products = ', '.join([str(product) for product in sale.product.all()])
        credit_bases = ', '.join([str(credit_base) for credit_base in sale.credit_base.all()])
        sales_data.append([
            sale.client.FIO,
            sale.client.phone_number,
            sale.sold_price,
            products,
            credit_bases,
            sale.discount,
            sale.info,
            sale.date.strftime('%Y-%m-%d'),
            sale.sold_user.username
        ])

        total_sold_price += sale.sold_price  # Accumulate total sold price

    # Calculate total discount
    total_discount = sum([sale.discount for sale in sales])

    # Append total row to sales_data
    sales_data.append([
        'Umumiy', '', total_sold_price, '', '',
        total_discount, '', '', ''
    ])

    df = pd.DataFrame(sales_data, columns=[
        'Mijoz', 'Mijoz raqami', 'Sotilgan narx', 'Mahsulotlar',
        'Kredit bazalar', 'Chegirma', 'Qo\'shimcha', 'Sana', 'Sotuvchi'
    ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={from_date}-{to_date}.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sales')
        worksheet = writer.sheets['Sales']

        for column in worksheet.columns:
            max_length = 0
            column = list(column)
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[get_column_letter(column[0].column)].width = adjusted_width

    return response
