from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm


'''
-----------
view templates for the Blog app
-----------
There will be 3 different views for the projects app:
1. blog_index will display a list of all your posts.
2. blog_detail will display the full post as well as comments and a form to allow users to create new comments.
3. blog_category will be similar to blog_index, but the posts viewed will only be of a specific category chosen by the user.
'''
# Create your views here.

def blog_index(request):
    '''Fetches all the blog data from sqlite db and renders into index page(blog_index.html)
    Params:
        request: http request object for GET/POST
    Return:
        rendered index page
    '''
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    '''Fetches all the blog category from sqlite db and renders into index page(blog_category.html)
    Params:
        request: http request object for GET/POST
        category: the category id
    Return:
        rendered index page
    '''
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, id):
    '''Fetches a particular blog detail data from sqlite db and renders into detail page(blog_detail.html)
    Params:
        request: http request object for GET/POST
        id: blog identifier as primary key
    Return:
        rendered index page
    '''
    post = Post.objects.get(pk=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)