# Generated by Django 3.1 on 2020-11-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20201123_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='deal',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Rent'), (2, 'Sale')], default=1, max_length=4, verbose_name='Deal'),
        ),
    ]
