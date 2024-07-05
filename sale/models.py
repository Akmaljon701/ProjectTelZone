from django.db import models
from client.models import Client
from product.models import Product
from django.core.exceptions import ValidationError
from user.models import CustomUser


class CreditBase(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Рассрочка Базы"


def validate_sold_price(value):
    if value <= 0:
        raise ValidationError('Цена продажи должна быть больше 0!')


class Sale(models.Model):
    product = models.ManyToManyField(Product, related_name='product_sales', verbose_name='Продукти')
    client = models.ForeignKey(Client, related_name='client_sales', on_delete=models.PROTECT, verbose_name='Клиент')
    sold_price = models.FloatField(verbose_name='Проданная цена', validators=[validate_sold_price])
    credit_base = models.ManyToManyField(CreditBase, related_name='credit_bases', verbose_name='Рассрочка Бази',
                                         blank=True)
    discount = models.FloatField(default=0)
    info = models.TextField(blank=True, null=True, verbose_name='Информация')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    sold_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Продажи"
