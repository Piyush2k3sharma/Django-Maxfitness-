from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.db import IntegrityError
from django.db.models import Q
from .models import Blog
import random
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def blog_home(request):
    if request.GET:
        user_query = request.GET.get('user_query')
        blog_list = models.Blog.objects.filter(Q(title__icontains=user_query) | Q(introduction__icontains=user_query)
                                       | Q(sub_heading1__icontains=user_query)| Q(sub_heading2__icontains=user_query)| 
                                       Q(sub_heading3__icontains=user_query)| Q(sub_heading4__icontains=user_query)).all()
    else:
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
        'blog_list' : blog
    }
    return render(request,'Blog/view_blogs.html',context=data)

def delete_blog(request,blog_id):
    blog = Blog.objects.get(blog_id=blog_id)
    blog.delete()
    return redirect('Blog:blogapp')

def update_blog(request,blog_id):
    blog = Blog.objects.get(blog_id=blog_id)
    data = {
        'blog_list' : blog
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


def login_user(request):
    if request.method=='POST':
        msg = {}
        email = request.POST.get('email')
        password = request.POST.get('password')

        if all([email,password]):
            is_valid_email = models.Bloggers.objects.filter(email=email).exists()
            if is_valid_email:
                blogger = models.Bloggers.objects.get(email=email)
                is_valid_password = check_password(password, blogger.password)
                if is_valid_password:
                    request.session['blogger_id'] = blogger.blogger_id
                    request.session['profile_pic'] = blogger.profile_pic.url
                    return redirect('homepage')
                else:
                    msg['error'] = 'Invalid email or password'
            else:
                msg['error'] = 'Invalid email or password'
        else:
            msg['error'] = 'All fields are required'
        return render(request,"Blog/login.html",context=msg)
    return render(request,"Blog/login.html")


def signup_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        city = request.POST.get('city')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        msg = {}
        
        if all([first_name, last_name, email, country, city, password, confirm_password]):
            if password == confirm_password:
                try : 
                    profile_photo = request.FILES.get('profile_photo')

                    encrypted_password = make_password(password)

                    new_blogger = models.Bloggers()
                    new_blogger.first_name = first_name
                    new_blogger.last_name = last_name
                    new_blogger.email = email
                    new_blogger.country = country
                    new_blogger.city = city
                    new_blogger.password = encrypted_password
                    if profile_photo:
                        new_blogger.profile_pic = profile_photo
                    
                    new_blogger.save()
                    msg['success'] = 'User Created Successfully.'
                except IntegrityError as e:
                    msg['error'] = str(e)
            else:
                msg['error'] = 'Passwords Do Not Matched'
        else:
            msg['error'] = 'All Fields Are Required'
        return render(request,'Blog/signup.html',context=msg)

    return render(request,'Blog/signup.html')


def user_dashboard(request):
    return render(request,'user_dashboard.html')

def logout_user(request):
    if request.session.get('blogger_id'):
        del request.session['blogger_id']
        del request.session['profile_pic']
    return redirect('homepage')