from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=[('admin', 'admin'), ('worker', 'worker')])

    class Meta:
        verbose_name_plural = "Users"
