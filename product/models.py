from django.db import models

from client.models import Client


class Product(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    purchase_price = models.FloatField()
    percent = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    imei = models.BigIntegerField()     # str
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='on_sale', choices=[['on_sale', 'on_sale'], ['sold', 'sold']])
    client = models.ForeignKey(Client, related_name='products', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name_plural = "Products"


class Expense(models.Model):
    type = models.CharField(max_length=150)
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} - {self.price}'

    class Meta:
        verbose_name_plural = "Expenses"
