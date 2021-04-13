# Generated by Django 3.1 on 2021-01-07 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0042_auto_20210107_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='photos/feedback/avatar/%Y/%m/', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='img',
            field=models.ImageField(blank=True, upload_to='photos/feedback/main_photo/%Y/%m/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='feedbackimages',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/feedback/all_photos/%Y/%m/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='property',
            name='img',
            field=models.ImageField(blank=True, upload_to='photos/main_photo/%Y/%m/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='propertyimages',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/secondary_photo/%Y/%m/', verbose_name='Image'),
        ),
    ]