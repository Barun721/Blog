from django.shortcuts import render,redirect,get_object_or_404
from posts.models import Posts
from posts.forms import Post_form,Update_post
from django.shortcuts import redirect
from accounts import views

# Create your views here.
def news_post(request):
    values = Posts.objects.all()
    return render(request,'posts/posts_list.html',{'values':values})

def create_post(request):
    if request.method == "POST":
        form = Post_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:news_post')
    else:
        form = Post_form()
    return render(request,'posts/create_post.html',{'form':form})

def update_post(request,postid):
    instance = get_object_or_404(Posts,id=postid)
    if request.method == 'POST':
        form = Update_post(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('posts:my_post')
    else:
        form = Update_post(instance=instance)
    return render(request,'posts/update_post.html',{'form':form})

def my_post(request):
    values = Posts.objects.all()
    return render(request,'posts/my_post.html',{'values':values})

def post_delete_form(request,postid):
    form = Posts.objects.get(pk=postid)
    if request.method == 'POST':
        form.delete()
        return redirect('posts:my_post')
    else:
        form = Posts.objects.get(pk=postid)
    return render(request,'posts/delete_post.html',{'form':form})


