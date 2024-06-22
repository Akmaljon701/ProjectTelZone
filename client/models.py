from django.db import models
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if not value.isdigit() or len(value) != 9:
        raise ValidationError("Номер телефона не должен содержать менее 9 цифр. (например: 999961516)")


class Client(models.Model):
    FIO = models.CharField(max_length=60, verbose_name='Ф.И.О')
    phone_number = models.CharField(max_length=9, unique=True,
                                    verbose_name='Номер телефона', validators=[validate_phone_number])

    def __str__(self):
        return f'{self.FIO} - {self.phone_number}'

    class Meta:
        verbose_name_plural = "Клиенты"

