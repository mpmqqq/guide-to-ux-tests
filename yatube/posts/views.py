from django.shortcuts import render, get_object_or_404

from hw02_community.yatube.yatube.settings import MAX_POST_ON_PAGE

from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:MAX_POST_ON_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:MAX_POST_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
