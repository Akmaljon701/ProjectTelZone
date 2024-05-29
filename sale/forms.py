from django.forms import ModelForm, ValidationError, FloatField, CharField
from sale.models import Sale, CreditBase


class CreditBaseAdminForm(ModelForm):
    class Meta:
        model = CreditBase
        fields = ['name']

    name = CharField(label='Название')


class SaleAdminForm(ModelForm):
    class Meta:
        model = Sale
        exclude = ['date']

    sold_price = FloatField(label='Цена продажи')

    def clean(self):
        cleaned_data = super().clean()
        sold_price = cleaned_data.get('sold_price')
        if sold_price <= 0:
            raise ValidationError('Цена продажи должна быть больше 0!')
        return cleaned_data
