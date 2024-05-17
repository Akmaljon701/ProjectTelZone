from django.db import models
from client.models import Client
from product.models import Product


class Sale(models.Model):
    product = models.ForeignKey(Product, related_name='product_sales', on_delete=models.PROTECT)
    client = models.ForeignKey(Client, related_name='client_sales', on_delete=models.PROTECT)
    sold_price = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} - {self.client}'

    class Meta:
        verbose_name_plural = "Продажи"
