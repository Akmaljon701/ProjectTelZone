# Generated by Django 5.0.4 on 2024-06-04 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_remove_sale_product_sale_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='credit_base',
            field=models.ManyToManyField(related_name='credit_bases', to='sale.creditbase'),
        ),
        migrations.DeleteModel(
            name='SaleCreditBase',
        ),
    ]
