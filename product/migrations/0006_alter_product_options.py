# Generated by Django 5.0.4 on 2024-05-29 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_delete_expense'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Продукты'},
        ),
    ]