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
    product = models.ManyToManyField(Product, related_name='product_sales')
    client = models.ForeignKey(Client, related_name='client_sales', on_delete=models.PROTECT)
    sold_price = models.FloatField()
    credit_base = models.ManyToManyField(CreditBase, related_name='credit_bases')
    info = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Продажи"
