from django.db import models


class Client(models.Model):
    FIO = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return f'{self.FIO} - {self.phone_number}'

    class Meta:
        verbose_name_plural = "Clients"

