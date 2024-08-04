from django.contrib import admin

# Register your models here.
from .models import Student, BlogPost

admin.site.register(Student)
admin.site.register(BlogPost)
