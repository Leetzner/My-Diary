from django.shortcuts import render

from .models import Post


def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'my_diary/frontpage.html', {'posts': posts})
