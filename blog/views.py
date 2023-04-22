from django.shortcuts import render
from .models import Post

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    return render(request, "blog/frontpage.html", {"posts": posts})

def post_detail(request, slug):
    # if slug from the button is same as the slug in the database...
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
