from product.models import Product
from django.forms import ModelForm, CharField, ValidationError, FloatField


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['status']

    name = CharField(label='Название')
    purchase_price = FloatField(label='Цена покупки')
    percent = FloatField(label='Процент', required=False)
    price = FloatField(label='Цена', required=False)

    def clean(self):
        cleaned_data = super().clean()
        purchase_price = cleaned_data.get('purchase_price')
        percent = cleaned_data.get('percent')
        price = cleaned_data.get('price')

        if percent and price:
            raise ValidationError('Вы не можете указать одновременно процент и цену. Пожалуйста, введите только один!')

        if not percent and not price:
            raise ValidationError('Вы должны указать либо процент, либо цену!')

        if percent:
            if percent <= 0:
                raise ValidationError('Процент должен быть больше 0!')
            price = purchase_price + ((purchase_price * percent) / 100)
            cleaned_data['price'] = price

        elif price:
            if purchase_price >= price:
                raise ValidationError('Цена не может быть меньше или равна цене покупки!')
            difference = price - purchase_price
            percent = (difference * 100) / purchase_price
            cleaned_data['percent'] = percent
        else:
            raise ValidationError('Неожиданная ошибка!')

        return cleaned_data
