# Generated by Django 3.1 on 2020-11-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20201125_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='deal',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale')], default='R', max_length=4, verbose_name='Deal'),
        ),
    ]
