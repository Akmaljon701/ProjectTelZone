from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
    purchase_price = models.FloatField()
    percent = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    imei = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='on_sale', choices=[['on_sale', 'on_sale'], ['sold', 'sold']])

    def __str__(self):
        return f'{self.name} - {self.price} - {self.count}'

    class Meta:
        verbose_name_plural = "Продукты"
