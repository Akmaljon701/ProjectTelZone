# Generated by Django 5.0.4 on 2024-05-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_discount_alter_product_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='client',
        ),
        migrations.AlterField(
            model_name='product',
            name='imei',
            field=models.CharField(max_length=100),
        ),
    ]