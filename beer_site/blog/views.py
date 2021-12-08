from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .utils import *
from .forms import TagForm, PostForm
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_form.html'


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'

class PostDelete(LoginRequiredMixin, ObjectsDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    link = 'posts_list_url'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
   model_form = TagForm
   template = 'blog/tag_form.html'


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'


class TagDelete(LoginRequiredMixin, ObjectsDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    link = 'tags_list_url'












