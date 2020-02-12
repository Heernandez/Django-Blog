from django.shortcuts import render

# Create your views here.  using a function or a class
from .models import Post


def list_post(request):
    #context is a dictionary of keys and values 
    posts = Post.objects.all()
    context = { "name": "Luis",
                "post_list":posts
            }
    return render(request,"posts/post_list.html",context)