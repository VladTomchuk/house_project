# Generated by Django 3.1 on 2020-11-23 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20201123_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='property_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.property'),
        ),
    ]
