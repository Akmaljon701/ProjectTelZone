# Generated by Django 5.0.4 on 2024-06-17 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_can_create', models.BooleanField(default=False)),
                ('product_can_update', models.BooleanField(default=False)),
                ('product_can_view', models.BooleanField(default=True)),
                ('client_can_create', models.BooleanField(default=False)),
                ('client_can_update', models.BooleanField(default=False)),
                ('client_can_view', models.BooleanField(default=True)),
                ('sale_can_create', models.BooleanField(default=False)),
                ('sale_can_update', models.BooleanField(default=False)),
                ('sale_can_view', models.BooleanField(default=True)),
                ('user_can_create', models.BooleanField(default=False)),
                ('user_can_update', models.BooleanField(default=False)),
                ('user_can_view', models.BooleanField(default=True)),
                ('dashboard_can_view', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
