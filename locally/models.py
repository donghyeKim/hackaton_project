from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

  
class Wish(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    body = models.TextField()

class Comment(models.Model):
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    
class Blog_10(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ManyToManyField(User, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
        
class Blog_20(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ManyToManyField(User, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
        
class Blog_30(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ManyToManyField(User, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
        
        
class Blog_40(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ManyToManyField(User, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
        
class Blog_50(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ManyToManyField(User, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
        
class Search(models.Model):
    search_title = models.CharField(max_length=20) 
    
class buy(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    body = models.TextField()
    
#     #수정해야함!!
# class Post(models.Model):
# 	title = models.CharField(max_length=100)
#     profile_pic = models.ImageField(upload_to="blog/profile_pic")
# 	# 저장경로 : MEDIA_ROOT/blog/profile_pic/xxxx.jpg 경로에 저장
# 	# DB필드 : 'MEDIA_URL/blog/profile_pic/xxxx.jpg' 문자열 저장
# 	photo = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")
# 	# 저장경로 : MEDIA_ROOT/blog/2017/05/10/xxxx.jpg 경로에 저장
# 	# DB필드 : 'MEDIA_URL/blog/2017/05/10/xxxx.jpg' 문자열 저장

class Post(models.Model): 
    title = models.CharField(max_length=50) 
    marketbuy_img = models.ImageField(upload_to='marketsell-images/') 
