# Generated by Django 3.1.2 on 2020-12-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0013_auto_20201217_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='cpu',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Procesador'),
        ),
        migrations.AddField(
            model_name='computer',
            name='gpu',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tarjeta Grafica'),
        ),
    ]
