from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import locally.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', locally.views.home, name="home"),
    path('choice/', locally.views.choice, name="choice"),
    path('site/', locally.views.site, name="site"),
    path('10/', locally.views.ten, name="ten"),
    path('schedule/', locally.views.schedule, name="schedule"),
    path('wish/', locally.views.wish, name="wish"),
    path('market/', locally.views.market, name="market"),
    path('job/', locally.views.job, name="job"),
    path('guide/', locally.views.guide, name="guide"),
    path('write/', locally.views.write, name="write"),
    path('accounts/', include('accounts.urls')),
    
   
]
