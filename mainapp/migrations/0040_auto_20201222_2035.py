# Generated by Django 3.1 on 2020-12-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0039_auto_20201222_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='img',
            field=models.ImageField(blank=True, upload_to='photos/feedback/main_photo/%Y/%m/%d/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='photos/feedback/avatar/%Y/%m/%d/', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='feedbackimages',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/feedback/all_photos/%Y/%m/%d/', verbose_name='Image'),
        ),
    ]
