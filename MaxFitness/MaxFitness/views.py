from django.shortcuts import render,HttpResponse
from Blog.models import Blog

def home(request):
    blogs = Blog.objects.all().order_by("-post_date")[:3]
    data = {
        'blog_list' : blogs
    }
    return render(request,"home.html",context=data)
