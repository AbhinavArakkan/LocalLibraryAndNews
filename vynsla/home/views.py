from django.shortcuts import render,get_object_or_404
from . models import Member,images,NewsItem
from django.utils import timezone


# Create your views here.

def home(request):
    members = Member.objects.all()
    return render(request, 'home/home.html',{'members':members})

def News(request):
    news_list = NewsItem.objects.all
    return render(request, 'home/news.html',{'news_list':news_list})

def Images(request):
    imgs = list(images.objects.all())
    imgs.reverse()    
    return render(request, 'home/images.html',{'imgs':imgs})

def history(request):
    return render(request, 'home/history.html')

def news_detail(request, news_id):
    news_item = get_object_or_404(NewsItem, pk=news_id)
    return render(request, 'home/news_detail.html', {'news_item': news_item})