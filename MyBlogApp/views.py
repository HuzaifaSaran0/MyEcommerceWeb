from django.shortcuts import render
from .models import BlogPost
# from django.http import HttpResponse

# Create your views here.


# Create your views here.
def index(request):
    all_blogs = BlogPost.objects.all()
    # for cat in all_blogs:

    return render(request, 'blog/index.html', {"all_blogs": all_blogs})


def blogpost(request, my_id):
    all_blogs = BlogPost.objects.all()
    post = BlogPost.objects.filter(blog_id=my_id)
    prev_post = BlogPost.objects.filter(blog_id=my_id - 1).first()
    next_post = BlogPost.objects.filter(blog_id=my_id + 1).first()

    context = {
        'blogpost': post,
        'all_blogs': all_blogs,
        'prev_post_title': prev_post.title if prev_post else None,
        'next_post_title': next_post.title if next_post else None,
        'prev_post_id': prev_post.blog_id if prev_post else None,
        'next_post_id': next_post.blog_id if next_post else None,
    }
    return render(request, 'blog/blogpost.html', context)

    # return HttpResponse("Hello, world. You're at the MyBlogApp."),
