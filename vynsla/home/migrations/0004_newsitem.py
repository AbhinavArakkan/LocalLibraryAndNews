# Generated by Django 4.2.1 on 2023-10-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_images_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='news_images/')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
