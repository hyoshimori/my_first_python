from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment

from blog.forms import CommentForm

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    return render(request, "blog/frontpage.html", {"posts": posts})

def post_detail(request, slug):
    # if slug from the button is same as the slug in the database...
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # This is to add add post info for the comment
            comment.post = post
            comment.save()

            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()
    return render(request, "blog/post_detail.html", {"post": post, "form": form})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_slug = comment.post.slug
    if request.user.username == comment.name or request.user.is_superuser:  # Compare request.user.username with comment.name
        comment.delete()
        return redirect("post_detail", slug=post_slug)
    else:
        return redirect("post_detail", slug=post_slug)
