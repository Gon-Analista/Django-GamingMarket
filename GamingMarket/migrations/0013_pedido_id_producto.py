# Generated by Django 4.1.2 on 2023-06-18 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamingMarket', '0012_alter_producto_stock_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='id_producto',
            field=models.ForeignKey(db_column='id_producto', default=12323, on_delete=django.db.models.deletion.CASCADE, to='GamingMarket.producto'),
            preserve_default=False,
        ),
    ]