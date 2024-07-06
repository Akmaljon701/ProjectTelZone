import pandas as pd
from django.db.models import Sum, F
from django.http import HttpResponse
from openpyxl.utils import get_column_letter
from rest_framework.decorators import api_view
from product.models import Product
from product.schemas import export_products_to_excel_schema
from utils.permissions import allowed_only_admin


@export_products_to_excel_schema
@api_view(['GET'])
@allowed_only_admin()
def export_products_to_excel(request):
    products = Product.objects.filter(status='on_sale').all()

    products_data = []
    total_profit = 0
    for product in products:
        profit = product.price - product.purchase_price
        products_data.append([
            product.name,
            product.purchase_price,
            product.percent,
            product.price,
            product.imei,
            product.date.strftime('%Y-%m-%d'),
            'sotuvda',
            profit
        ])
        total_profit += profit

    products_data.append([
        'Umumiy', '', '', '',
        '', '', '', total_profit
    ])

    df = pd.DataFrame(products_data, columns=[
        'Nomi', 'Olingan narx', 'Foiz',
        'Sotuv narx', 'IMEI', 'Sana', 'Status', 'Kutilyotgan foyda'
    ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=Mahsulot_qoldiqlari.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Products')
        worksheet = writer.sheets['Products']

        for column in worksheet.columns:
            max_length = 0
            column = list(column)
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[get_column_letter(column[0].column)].width = adjusted_width

    return response

