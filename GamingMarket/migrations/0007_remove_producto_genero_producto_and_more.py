# Generated by Django 4.1.2 on 2023-06-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamingMarket', '0006_alter_producto_genero_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='genero_producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='estado_pedido',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(max_length=30),
        ),
    ]
