from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.
def blog_home(request):
    return render(request, 'Blog/blogs.html')

def add_blog(request):
    if request.POST:

        msg = {

        }

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

            msg['success'] = "New Blog created Successfully"

            success_msg = {
                'success' : "Blog Created Successfully!!"
            }

        
        else:
            msg['error'] = "All fields are required"

        return render(request,'Blog/add_blog.html', msg)


    return render(request,'Blog/add_blog.html')