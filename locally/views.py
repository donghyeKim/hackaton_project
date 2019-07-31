from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog_10, Blog_20 , Blog_30, Blog_40, Blog_50, Wish, Comment, buy
from .forms import NewBlog_10, NewBlog_20, NewBlog_30, NewBlog_40, NewBlog_50, SearchForm
from .forms import NewWish, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def home(request):
    return render(request, 'locally/home.html')

def choice(request):
    return render(request, 'locally/choice.html')

def site(request):
    return render(request, 'locally/site.html')

def schedule(request):
    return render(request, 'locally/schedule.html')



def wish(request):
    wishs = Wish.objects
    wish_list=Wish.objects.all()
    paginator = Paginator(wish_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'locally/wish.html', {'wishs':wishs,'posts':posts})

def wishwrite(request):
    return render(request, 'locally/wishwrite.html')

def wishclick(request, wish_id):
    wish_wishclick = get_object_or_404(Wish, pk=wish_id)
    return render(request, 'locally/wishclick.html', {'wish': wish_wishclick})

def wishcreate(request):
    wish = Wish()
    wish.title = request.GET['title']
    wish.body = request.GET['body']
    wish.pub_date = timezone.datetime.now()
    wish.save()
    return redirect('/locally/' + str(wish.id))

def wishupdate(request, pk):
    wish = get_object_or_404(Wish, pk = pk)
    form = NewWish(request.POST, instance=wish)
    if form.is_valid():
        wish.save()
        return redirect('wish')
    return render(request,'locally/newform.html',{'form':form})

def wishdelete(request, pk):
    wish = get_object_or_404(Wish, pk = pk)
    wish.delete()
    return redirect('wish')

def comment_write(request, pk):
    wish = get_object_or_404(Wish, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.wish = wish
            comment.save()
            return redirect('/locally/' + str(wish.id))
    else:
        form = CommentForm()
    return redirect('/locally/' + str(wish.id))





def market(request):
    return render(request, 'locally/market.html')

def job(request):
    return render(request, 'locally/job.html')

def guide(request):
    return render(request, 'locally/guide.html')

def write(request):
    return render(request, 'locally/write.html')

def read_10(request):
    blogs = Blog_10.objects.all()
    return render(request, 'locally/10.html', {'blogs':blogs})

def read_20(request):
    blogs = Blog_20.objects.all()
    return render(request, 'locally/20.html', {'blogs':blogs})

def read_30(request):
    blogs = Blog_30.objects.all()
    return render(request, 'locally/30.html', {'blogs':blogs})

def read_40(request):
    blogs = Blog_40.objects.all()
    return render(request, 'locally/40.html', {'blogs':blogs})

def read_50(request):
    blogs = Blog_50.objects.all()
    return render(request, 'locally/50.html', {'blogs':blogs})


def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('ten')
    else:
        form = NewBlog()
        return render(request, 'locally/write.html', {'form':form})

    
    
def schedulebokji(request):
    return render(request, 'locally/schedulebokji.html')

def edit(request, post_id):
    edit_post = Post.objects.get(id=post_id)
    return render(request, 'locally/edit.html', {'post':edit_post})




def new_comment(request, post_id):
    comment = Comment()
    comment.writer = request.POST['writer']
    comment.content = request.POST['content']
    comment.post = get_object_or_404(Post, pk=post_id)
    comment.save()
    return redirect('detail', post_id)



#def like(request,post_id):
    #blog = get_object_or_404(Blog, pk = blog_id)
    #if blog.user.filter(username=request.user.username).exists():
      #  blog.user.remove(request.user)    
  #  else:
   #     blog.user.add(request.user)
   # blog.save()
   # return redirect('detail', blog_id)


def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    form = NewBlog(request.POST, instance = blog)
    if form.is_valid():
        form.save()
        return redirect('ten')
    return render(request, 'locally/write.html', {'form':form})
        
    





def delete(request, pk):
    delete_post=Blog.objects.get(pk=pk)
    delete_post.delete()
    return redirect('site')
#def index(request):
    #blogs = Blog.objects
    #blog_list = Blog.objects.all()
    #paginator = Paginator(blog_list, 2)
    #page = request.GET.get('page')
    #posts = paginator.get_page(page)
    #return render(request, 'funccrud/funccrud.html', {'blogs':blogs, 'posts':posts})

    
class SerachFormView():
    form_Class = SearchForm
    template_name = 'blog/search.html'

    def form_valid(self,form):
        word = '%s' %self.request.POST['word']
        post_list = Post.objects.filter(
            Q(title_icontains=word) | Q(content_icontains=word)
        ).distinct()
        context = {}
        context['object_list'] = post_list
        context['search_word'] = search_word
        return context
    
    
def market(request):
    return render(request,'locally/market.html')

def marketbuy(request):
    return render(request, 'locally/marketbuy.html')

def marketbuywrite(request):
    return render(request, 'locally/marketbuywrite.html')

def marketbuydetail(request):
    return render(request, 'locally/marketbuydetail.html')

def free(request):
    return render(request, 'locally/marketfree.html')

def sell(request):
    return render(request, 'locally/marketsell.html')

def marketsellwrite(request):
    return render(request, 'locally/marketsellwrite.html')

def apply(request):
    return render(request, 'locally/jobapply.html')

def offer(request):
    return render(request, 'locally/joboffer.html')

def detail(request):
    return render(request,'locally/detail.html') 

def sell_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'hotel_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 
