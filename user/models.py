from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'admin'),
        ('worker', 'worker')
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    class Meta:
        verbose_name_plural = "Пользователи"
