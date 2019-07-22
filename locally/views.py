from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog



# Create your views here.


def home(request):
    return render(request, 'locally/home.html')

def choice(request):
    return render(request, 'locally/choice.html')

def site(request):
    return render(request, 'locally/site.html')

def login(request):
    return render(request, 'locally/login.html')

def ten(request):
    blogs = Blog.objects.all()
    return render(request, 'locally/10.html', {'blogs':blogs})

def schedule(request):
    return render(request, 'locally/schedule.html')

def wish(request):
    return render(request, 'locally/wish.html')

def market(request):
    return render(request, 'locally/market.html')

def job(request):
    return render(request, 'locally/job.html')

def guide(request):
    return render(request, 'locally/guide.html')

def write(request):
    return render(request, 'locally/write.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'locally/site.html', {'blogs':blogs})

def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('10')
    else:
        form = NewBlog()
        return render(request, 'locally/write.html', {'form':form})
        
        
        
        
        
def login(request):
    return render(request, 'login.html')


#def index(request):
    #blogs = Blog.objects
    #blog_list = Blog.objects.all()
    #paginator = Paginator(blog_list, 2)
    #page = request.GET.get('page')
    #posts = paginator.get_page(page)
    #return render(request, 'funccrud/funccrud.html', {'blogs':blogs, 'posts':posts})




        
        
        











