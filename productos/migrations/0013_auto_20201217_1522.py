# Generated by Django 3.1.2 on 2020-12-17 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_auto_20201217_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computerpricer',
            old_name='Computer',
            new_name='computer',
        ),
    ]