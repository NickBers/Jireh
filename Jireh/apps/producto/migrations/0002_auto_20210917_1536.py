# Generated by Django 3.2.7 on 2021-09-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='producto',
            name='precioNoIVa',
            field=models.FloatField(null=True),
        ),
    ]