from datetime import datetime

import pandas as pd
from django.http import HttpResponse
from sale.models import Sale, CustomUser


def export_sales_to_excel(request):
    user = request.query_params.get('user')
    from_date = request.query_params.get('from_date')
    to_date = request.query_params.get('to_date')

    if not user or not from_date or not to_date:
        return HttpResponse('user, from_date, and to_date are required.', status=400)

    try:
        from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
        to_date = datetime.strptime(to_date, '%Y-%m-%d').date()
    except ValueError:
        return HttpResponse({'detail': 'from_date and to_date date format is wrong!'}, status=422)

    if from_date > to_date:
        return HttpResponse({'detail': 'from_date must be less than to_date!'}, status=422)

    sold_user = CustomUser.objects.get(id=user)

    sales = Sale.objects.filter(
        sold_user=sold_user,
        date__range=[from_date, to_date]
    ).select_related('client', 'sold_user').prefetch_related('product', 'credit_base')

    sales_data = []
    for sale in sales:
        products = ', '.join([str(product) for product in sale.product.all()])
        credit_bases = ', '.join([str(credit_base) for credit_base in sale.credit_base.all()])
        sales_data.append([
            sale.id,
            sale.client.name,
            sale.sold_price,
            products,
            credit_bases,
            sale.info,
            sale.date,
            sale.sold_user.username
        ])

    df = pd.DataFrame(sales_data, columns=[
        'Sale ID', 'Client', 'Sold Price', 'Products', 'Credit Bases', 'Info', 'Date', 'Sold User'
    ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=sales.xlsx'

    df.to_excel(response, index=False)

    return response