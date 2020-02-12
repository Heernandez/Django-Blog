from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.  using a function or a class
from .models import Post
from .forms import PostForm

def list_post(request):
    #context is a dictionary of keys and values 
    posts = Post.objects.all()
    context = { "name": "Luis",
                "post_list":posts
            }
    return render(request,"post_list.html",context)


def post_detail(request,post_id):
    #print("###########################\nLO QUE RECIBO ES UN {}".format(type(post_id)))
    try:
        post_id = int(post_id)
    except:
        return render(request,"ERROR.html")

    try:
        post = Post.objects.get(id = int(post_id))
    except: 
        post = Post()
        post.id = 0
       
    context ={
     'post' : post
    }
    return render(request,"post_detail.html",context)
    
    
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')
    context ={
        "form":form
    }

    return render(request,"post_create.html",context)
