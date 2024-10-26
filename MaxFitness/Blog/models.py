from django.db import models

# Create your models here.

class Bloggers(models.Model):
    blogger_id = models.AutoField(primary_key=True,unique=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    profile_pic = models.ImageField(upload_to="bloggers_profiles",null=True,default='bloggers_profiles/default.jpg')
    password = models.CharField(max_length=3000, editable=False)

    def __str__(self):
        return f"Blogger Id : {self.blogger_id} , First name : {self.first_name} , Last name : {self.last_name}"

class Blog(models.Model):

    CATEGORY_CHOICES = [
        ("Weight loss","Weight loss"),
        ("Weight gain","Weight gain"),
        ("Food","Food"),
        ("Health","Health"),
        ("Muscle gain","Muscle gain"),
        ("Yoga","Yoga"),
    ]

    blog_id = models.AutoField(primary_key=True,unique=True)
    title = models.CharField(max_length=3000)
    category = models.CharField(max_length=300,choices=CATEGORY_CHOICES)
    introduction = models.TextField(max_length=6000)
    sub_heading1 = models.CharField(max_length=1000)
    content1 = models.CharField(max_length=10000)
    sub_heading2 = models.CharField(max_length=1000)
    content2 = models.CharField(max_length=10000)
    sub_heading3 = models.CharField(max_length=1000)
    content3 = models.CharField(max_length=10000)
    sub_heading4 = models.CharField(max_length=1000)
    content4 = models.CharField(max_length=10000)
    post_date = models.DateTimeField(auto_now=True)
    published_by = models.ForeignKey(Bloggers,on_delete=models.CASCADE,null=True)
    # cascade ,mtbl if user delete ta ohde likhe sare blogs get deleted

    def __str__(self):
        return f"Blog id : {self.blog_id} , category : {self.category}"
    

# if database ch kuch changes kite ta migrations bnania paindia taki changes apply hoje 