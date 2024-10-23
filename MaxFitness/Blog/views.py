from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.db import IntegrityError
from .models import Blog
import random

# Create your views here.
def blog_home(request):
    blog_list = Blog.objects.all()
    random.randint(1,6)
    return render(request, 'Blog/blogs.html',{'blog_list' : blog_list})

def add_blog(request):
    if request.POST:

        msg = {}

        title = request.POST.get('title')
        category = request.POST.get('category')
        introduction = request.POST.get('introduction')
        sub_heading1 = request.POST.get('subheading1')
        sub_heading2 = request.POST.get('subheading2')
        sub_heading3 = request.POST.get('subheading3')
        sub_heading4 = request.POST.get('subheading4')
        content1 = request.POST.get('content1')
        content2 = request.POST.get('content2')
        content3 = request.POST.get('content3')
        content4 = request.POST.get('content4')

        if all([title, category, introduction, sub_heading1, sub_heading2, sub_heading3, sub_heading4, content1, content2, content3, content4]):
            # new_blog = models.Blog()
            # new_blog.title = title
            # new_blog.category = category
            # new_blog.introduction = introduction
            # new_blog.sub_heading1 = sub_heading1
            # new_blog.sub_heading2 = sub_heading2
            # new_blog.sub_heading3 = sub_heading3
            # new_blog.sub_heading4 = sub_heading4
            # new_blog.content1 = content1
            # new_blog.content2 = content2
            # new_blog.content3 = content3
            # new_blog.content4 = content4
            # new_blog.save()
            models.Blog.objects.create(title=title,category=category,introduction=introduction,
                                       sub_heading1=sub_heading1,sub_heading2=sub_heading2,sub_heading3=sub_heading3,
                                       sub_heading4=sub_heading4,content1=content1,content2=content2,content3=content3,
                                       content4=content4)
            
            msg['success'] = "New Blog created Successfully"

            success_msg = {
                'success' : "Blog Created Successfully!!"
            }

        
        else:
            msg['error'] = "All fields are required"

        return render(request,'Blog/add_blog.html', msg)


    return render(request,'Blog/add_blog.html')

def view_blog(request,blog_id):
    blog = Blog.objects.get(blog_id=blog_id)
    data = {
        'blog' : blog
    }
    return render(request,'Blog/view_blogs.html',context=data)

def delete_blog(request,blog_id):
    blog = Blog.objects.get(blog_id=blog_id)
    blog.delete()
    return redirect('Blog:blogapp')

def update_blog(request,blog_id):
    blog = Blog.objects.get(blog_id=blog_id)
    data = {
        'blog' : blog
    }
    if request.POST:

        msg = {}

        title = request.POST.get('title')
        category = request.POST.get('category')
        introduction = request.POST.get('introduction')
        sub_heading1 = request.POST.get('subheading1')
        sub_heading2 = request.POST.get('subheading2')
        sub_heading3 = request.POST.get('subheading3')
        sub_heading4 = request.POST.get('subheading4')
        content1 = request.POST.get('content1')
        content2 = request.POST.get('content2')
        content3 = request.POST.get('content3')
        content4 = request.POST.get('content4')

        if all([title, category, introduction, sub_heading1, sub_heading2, sub_heading3, sub_heading4, content1, content2, content3, content4]):
            try:                
                blog.title = title
                blog.category = category
                blog.introduction = introduction
                blog.sub_heading1 = sub_heading1
                blog.sub_heading2 = sub_heading2
                blog.sub_heading3 = sub_heading3
                blog.sub_heading4 = sub_heading4
                blog.content1 = content1
                blog.content2 = content2
                blog.content3 = content3
                blog.content4 = content4
                blog.save()
            except IntegrityError as e:
                data['error'] = str(e)
        else:
            data['error'] = "All fields are required"
    return render(request,'Blog/update_blogs.html',context=data)