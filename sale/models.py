from django.db import models
from client.models import Client
from product.models import Product


class CreditBase(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Рассрочка Базы"


class Sale(models.Model):
    product = models.ForeignKey(Product, related_name='product_sales', on_delete=models.PROTECT)
    client = models.ForeignKey(Client, related_name='client_sales', on_delete=models.PROTECT)
    credit_base = models.ForeignKey(CreditBase, related_name='credit_sales', on_delete=models.PROTECT,
                                    blank=True, null=True)
    info = models.TextField(default='')
    sold_price = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} - {self.client}'

    class Meta:
        verbose_name_plural = "Продажи"
