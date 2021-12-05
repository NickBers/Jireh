# Generated by Django 3.2.7 on 2021-12-01 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0004_alter_venta_iva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
