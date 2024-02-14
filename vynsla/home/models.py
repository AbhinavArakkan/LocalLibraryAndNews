from django.db import models

class Member(models.Model):
    position = models.CharField(max_length=100) 
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='member_imgs')
    

class images(models.Model):
    img = models.ImageField(upload_to='imgs')

class NewsItem(models.Model):
    headline = models.CharField(max_length=500)
    image = models.ImageField(upload_to='news_images/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.headline
    