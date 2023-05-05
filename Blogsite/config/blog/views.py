from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Blog , Category
# Create your views here.

def home(request):
    blog_list = Blog.objects.published()
    paginator = Paginator(blog_list, 3)  
    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)
    context = {
        'blogs':blogs,
    }
    return render(request,'index.html',context)


def detail(request,pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog':blog
    }
    return render(request,'post.html',context)


def category(request,slug,page=1):
    category = Category.objects.get(slug=slug,is_active=True)
    blogs_list = category.blogs.published()
    paginator = Paginator(blogs_list, 2)  
    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)
    context = {
        'category': category,
        'blogs':blogs
    }
    return render(request,'category.html',context)