# Generated by Django 4.1.2 on 2023-06-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamingMarket', '0011_remove_pedido_id_inventario_producto_stock_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock_producto',
            field=models.IntegerField(),
        ),
    ]