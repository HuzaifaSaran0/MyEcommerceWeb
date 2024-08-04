from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    # image = models.ImageField()
    file = models.FileField()


class BlogPost(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to="static/shop", default="")
    intro_para = models.CharField(max_length=500)
    heading = models.CharField(max_length=200)
    para2 = models.CharField(max_length=500)
    image2 = models.ImageField(upload_to="static/shop", default="")
    list_content = models.CharField(max_length=1000, default="")
    para3 = models.CharField(max_length=500)
    image3 = models.ImageField(upload_to="static/shop", default="")
    conclusion = models.CharField(max_length=500)
    Published_date = models.DateTimeField()

    def __str__(self):
        return self.title
