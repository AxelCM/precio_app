# Generated by Django 3.1.2 on 2020-12-16 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_auto_20201215_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='description',
            field=models.IntegerField(default=12, verbose_name='Tam. Descripcion'),
        ),
        migrations.AlterField(
            model_name='size',
            name='horizontal',
            field=models.IntegerField(verbose_name='Medida Horizontal'),
        ),
        migrations.AlterField(
            model_name='size',
            name='price',
            field=models.IntegerField(default=12, verbose_name='Tam. Precio'),
        ),
        migrations.AlterField(
            model_name='size',
            name='title',
            field=models.IntegerField(default=24, verbose_name='Tam. Titulo'),
        ),
        migrations.AlterField(
            model_name='size',
            name='vertical',
            field=models.IntegerField(verbose_name='Medida Vertical'),
        ),
    ]
