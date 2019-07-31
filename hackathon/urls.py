from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import locally.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', locally.views.home, name="home"),
    path('choice/', locally.views.choice, name="choice"),
    path('site/', locally.views.site, name="site"),
    path('10/', locally.views.read_10, name="ten"),
    path('20/', locally.views.read_20, name="twenty"),
    path('30/', locally.views.read_30, name="thirty"), 
    path('40/', locally.views.read_40, name="forty"), 
    path('50/', locally.views.read_50, name="fifty"),  
    path('schedule/', locally.views.schedule, name="schedule"),
    
    path('wish/', locally.views.wish, name="wish"),
    path('locally/<int:wish_id>/', locally.views.wishclick, name="wishclick"),
    path('locally/wishwrite/', locally.views.wishwrite, name="wishwrite"),      
    path('locally/wishcreate/', locally.views.wishcreate, name="wishcreate"),
    path('wishupdate/<int:pk>', locally.views.wishupdate, name="wishupdate"),
    path('wishdelete/<int:pk>', locally.views.wishdelete, name="wishdelete"),   
    path('comment_write/<int:pk>', locally.views.comment_write, name="comment_write"),
    
    path('market/', locally.views.market, name="market"),
    path('job/', locally.views.job, name="job"),
    path('guide/', locally.views.guide, name="guide"),
    path('write/', locally.views.create, name="write"),
    path('accounts/', include('accounts.urls')),
    path('schedulebokji/', locally.views.schedulebokji, name="schedulebokji"),
    path('write/', locally.views.create, name="write"),
    path('update/<int:pk>', locally.views.update, name="update"),
    path('delete/<int:pk>', locally.views.delete, name="delete"),
    path('market/buy', locally.views.marketbuy, name="marketbuy"),
    path('market/buy/write', locally.views.marketbuywrite, name="marketbuywrite"),
    path('market/buy/detail', locally.views.marketbuydetail,name="marketbuydetail"),
    path('market/sell', locally.views.sell, name="sell"),
    path('market/sell/write', locally.views.marketsellwrite, name="marketsellwrite"),
    path('market/free', locally.views.free, name="free"),
    path('job/apply', locally.views.apply, name="apply"),
    path('job/offer', locally.views.offer, name="offer"),
    path('10/detail', locally.views.detail, name="detail"),
    path('sell_image_upload', sell_image_view, name = 'sell_image_upload'), 
    path('success', success, name = 'success'), 
]