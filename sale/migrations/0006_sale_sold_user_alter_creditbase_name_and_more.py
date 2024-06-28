# Generated by Django 5.0.4 on 2024-06-28 10:29

import django.db.models.deletion
import sale.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_client_fio_alter_client_phone_number'),
        ('product', '0007_alter_product_count_alter_product_date_and_more'),
        ('sale', '0005_sale_credit_base_delete_salecreditbase'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='sold_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='creditbase',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_sales', to='client.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='credit_base',
            field=models.ManyToManyField(related_name='credit_bases', to='sale.creditbase', verbose_name='Рассрочка Бази'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.ManyToManyField(related_name='product_sales', to='product.product', verbose_name='Продукти'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sold_price',
            field=models.FloatField(validators=[sale.models.validate_sold_price], verbose_name='Проданная цена'),
        ),
    ]
