# Generated by Django 4.1.2 on 2023-06-14 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamingMarket', '0009_rename_estado_pedido_producto_genero_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_cliente',
            field=models.AutoField(db_column='idCliente', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen_producto',
            field=models.ImageField(null=True, upload_to='Producto'),
        ),
    ]
