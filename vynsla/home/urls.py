from django.urls import path
from . views import home,history,News,Images,news_detail
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',home,name='home'),
    path('ചരിത്രം',history,name='history'),
    path('വാർത്തകൾ',News,name='news'),
    path('Images',Images,name='images'),
    path('<int:news_id>/', news_detail, name='news_detail'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
