# Generated by Django 4.2.1 on 2023-10-11 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_newsitem_content_alter_images_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='content',
        ),
    ]
