# Generated by Django 4.2.7 on 2024-03-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_images_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(upload_to='imgs'),
        ),
        migrations.AlterField(
            model_name='member',
            name='img',
            field=models.ImageField(upload_to='member_imgs'),
        ),
    ]
