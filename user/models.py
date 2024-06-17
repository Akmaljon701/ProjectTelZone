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


class CustomUserPermission(models.Model):
    user = models.OneToOneField(CustomUser, related_name='permission_fields', on_delete=models.CASCADE)

    product_can_create = models.BooleanField(default=False)
    product_can_update = models.BooleanField(default=False)
    product_can_view = models.BooleanField(default=True)

    client_can_create = models.BooleanField(default=False)
    client_can_update = models.BooleanField(default=False)
    client_can_view = models.BooleanField(default=True)

    sale_can_create = models.BooleanField(default=False)
    sale_can_update = models.BooleanField(default=False)
    sale_can_view = models.BooleanField(default=True)

    credit_base_can_create = models.BooleanField(default=False)
    credit_base_can_update = models.BooleanField(default=False)
    credit_base_can_view = models.BooleanField(default=True)

    user_can_create = models.BooleanField(default=False)
    user_can_update = models.BooleanField(default=False)
    user_can_view = models.BooleanField(default=True)

    dashboard_can_view = models.BooleanField(default=True)
    expense_can_create = models.BooleanField(default=False)
    expense_can_update = models.BooleanField(default=False)
    expense_can_view = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
