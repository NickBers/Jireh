# Generated by Django 3.2.7 on 2021-09-17 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, verbose_name='Nombre')),
                ('empresa', models.CharField(max_length=150, verbose_name='Nombre')),
                ('email', models.CharField(max_length=150, null=True, verbose_name='Nombre')),
                ('numero', models.CharField(max_length=150, null=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
