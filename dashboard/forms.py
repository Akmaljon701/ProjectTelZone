from django.forms import ModelForm, CharField, ValidationError, FloatField
from dashboard.models import Expense


class ExpenseAdminForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['type', 'price']

    type = CharField(label="Тип")
    price = FloatField(label="Цена")

    def clean(self):
        cleaned_data = super().clean()
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Цена не может быть 0 или меньше 0!")
        return cleaned_data

