from django.db import models
from django.core.exceptions import ValidationError


def positive_validator(value):
    if value <= 0:
        raise ValidationError("Цена не может быть 0 или меньше 0!")


class Expense(models.Model):
    type = models.CharField(max_length=150, verbose_name='Тип')
    price = models.FloatField(verbose_name='Цена', validators=[positive_validator])
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f'{self.type} - {self.price}'

    class Meta:
        verbose_name_plural = "Затраты"
