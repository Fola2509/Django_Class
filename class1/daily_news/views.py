from django.shortcuts import render, redirect
from .form import BlogForm
from .models import Blog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
#  Display Hello World

def homepage(request):
    blogs_post = Blog.objects.all()
    return render(request, "daily_news/homepage.html", context={'blogs': blogs_post})




# IF THE USER SUBMIT A FOrm
@login_required()
def blog_post(request):
    # COLLECT ALL THE DATA INPUT``
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        # CHECK IF THE INPUT IS CORRECT
        if form.is_valid():
            # SAVE THE DATA TO THE DATABASE
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            # WHAT NEXT?
            # REDIRECT
            return redirect("/")
    return render(request, "daily_news/createblog.html")
# if request.method == 'post'
# form = BlogForm(request.data)

# how to direct user to a specific blog post
# check the database to see if there's any blog post with that ID exist
# conditionally checks if it exist:
# Render the page with the blog post
# else
# Redirect the user to /not_found
def article(request, pk):
    # Scan through the blog table
    # and get blog_posts whose its ID 
    # is the same as the primary_key
    blog_post = Blog.objects.filter(id=pk)
    if blog_post.exists():
        return render(request, "daily_news/article.html", context={"blog": blog_post.first()})
    else:
        return redirect("/not_found")

def not_found(request):
    return HttpResponse("Not found")

@login_required()
def delete_blog(request, pk):
    if request.method == "POST":
        post = Blog.objects.filter(id=pk).first()
        if post is not None:
            if post.author != request.user:
                  return HttpResponse("Permission Denied. You're not the owner of the blog post.", status=403)  
            post.delete()
        return redirect("/")



@login_required
def edit_blog(request, pk):
    blog_posts = Blog.objects.filter(id=pk)

    if not blog_posts.exists():
        return redirect("/not-found")
    
    blog_post = blog_posts.first()
    if blog_post.author != request.user:
        return HttpResponse("Permission Denied. You're not the owner of the blog post.", status=403)

    # HTTP RESPONSES:
    # HTTP 1xx ---> info
    # HTTP 2xx ---> request ok
    # HTTP 3x ---> redirection
    # HTTP 4xx ---> client/user error
    # HTTP 5xx ---> server
    form = BlogForm(instance=blog_post)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog_post)
        if form.is_valid():
            _post = form.save(commit=False)  # commit means not to save the form yet and we still have something to add to the form
            _post.author = request.user
            _post.published_at = blog_post.published_at
            _post.save()
            
            return redirect('read-blog', pk=blog_post.pk)

    return render(request, "daily_news/edit_blog.html", {"blog_post": blog_post, 'form': form})


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
     form = UserCreationForm(request.POST)
    #  usercreationform item - username, password, email, 
    if form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    user= request.user
    user_posts = user.blog_set.all()
    return render(request, "registration/profile.html", context={'blogs': user_posts})
    
    
    
