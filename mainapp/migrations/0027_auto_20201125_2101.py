# Generated by Django 3.1 on 2020-11-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_auto_20201125_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='deal',
            field=models.CharField(choices=[('Rent', 'RENT'), ('Sale', 'SALE')], default='Rent', max_length=14, verbose_name='Deal'),
        ),
    ]
