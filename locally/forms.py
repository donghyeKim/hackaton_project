from django import forms
from .models import Blog_10, Blog_20, Blog_30, Blog_40, Blog_50, Wish, Comment, buy
from .models import Search
from django.db import models

  
class NewBlog_10(forms.ModelForm):
    class Meta:
        model = Blog_10
        fields = ['title', 'body']
class NewBlog_20(forms.ModelForm):
    class Meta:
        model = Blog_20
        fields = ['title', 'body']
class NewBlog_30(forms.ModelForm):
    class Meta:
        model = Blog_30
        fields = ['title', 'body']
class NewBlog_40(forms.ModelForm):
    class Meta:
        model = Blog_40
        fields = ['title', 'body']
class NewBlog_50(forms.ModelForm):
    class Meta:
        model = Blog_50
        fields = ['title', 'body']

class NewWish(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['title','body']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_contents']        
        
        
class SearchForm(forms.ModelForm):
    model = Search
    word = ['search_title']
        
        
#class CommentForm(forms.ModelForm):
    #class Meta:
     #  model = Comment
   # fields = ('author','text',)

class NewBuy(forms.ModelForm):
	class Meta:
		model = buy
		fields = ['title','body']
        
from django import forms 
from .models import *
  
class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = ['title', 'marketbuy_img'] 