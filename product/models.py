from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    count = models.PositiveIntegerField(verbose_name='Шт')
    purchase_price = models.FloatField(verbose_name='Цена покупки')
    percent = models.FloatField(blank=True, null=True, verbose_name='Процент')
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')
    imei = models.CharField(max_length=100, unique=True, verbose_name='IMEI')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    status = models.CharField(max_length=20, default='on_sale',
                              choices=[['on_sale', 'on_sale'], ['sold', 'sold']], verbose_name='Статус')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Продукты"
