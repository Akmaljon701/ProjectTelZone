from django.db import models


class Expense(models.Model):
    type = models.CharField(max_length=150)
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} - {self.price}'

    class Meta:
        verbose_name_plural = "Затраты"
