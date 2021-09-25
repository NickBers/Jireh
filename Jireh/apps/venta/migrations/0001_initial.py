# Generated by Django 3.2.7 on 2021-09-23 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('subtotal', models.FloatField()),
                ('iva', models.FloatField()),
                ('total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.clientes')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Detalles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('monto', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.venta')),
            ],
            options={
                'verbose_name': 'Detalle',
                'verbose_name_plural': 'Detalles',
                'ordering': ['-created'],
            },
        ),
    ]
