# Generated by Django 4.1.2 on 2023-06-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamingMarket', '0004_alter_pedido_estado_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='genero_producto',
            field=models.IntegerField(null=True),
        ),
    ]
