from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request):
    blogs=Blog.objects.all()
    return render(request,'home.html',{'blogs_key':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return  render(request,'detail.html',{'blogContents':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title= request.POST['title']
    new_blog.writer=request.POST['writer']
    new_blog.body=request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail',new_blog.id)

def edit(request,blog_id):
    edit_blog = Blog.objects.get(id=blog_id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,blog_id):
    update_blog=Blog.objects.get(id=blog_id)
    update_blog.title= request.POST['title']
    update_blog.writer=request.POST['writer']
    update_blog.body=request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail',update_blog.id)
def delete(request,blog_id):
    delete_blog=Blog.objects.get(id=blog_id)
    delete_blog.delete()
    return redirect('home')