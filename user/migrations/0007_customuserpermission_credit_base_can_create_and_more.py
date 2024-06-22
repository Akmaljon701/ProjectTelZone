# Generated by Django 5.0.4 on 2024-06-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_customuserpermission_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuserpermission',
            name='credit_base_can_create',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuserpermission',
            name='credit_base_can_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuserpermission',
            name='credit_base_can_view',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuserpermission',
            name='expense_can_create',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuserpermission',
            name='expense_can_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuserpermission',
            name='expense_can_view',
            field=models.BooleanField(default=True),
        ),
    ]