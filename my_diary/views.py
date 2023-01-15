from django.shortcuts import render

from .models import Post


def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'my_diary/frontpage.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'my_diary/post_detail.html', {'post': post})