# Generated by Django 3.1 on 2020-11-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20201125_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='province',
            field=models.CharField(choices=[('Barcelona', 'Barcelona'), ('Girona', 'Girona'), ('Lleida', 'Lleida'), ('Tarragona', 'Tarragona')], default='Barcelona', max_length=100, verbose_name='Province'),
        ),
    ]
