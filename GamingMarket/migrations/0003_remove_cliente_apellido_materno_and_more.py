# Generated by Django 4.1.2 on 2023-06-13 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamingMarket', '0002_cliente_inventario_pedido_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apellido_materno',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='apellido_paterno',
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
