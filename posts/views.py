from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from posts.forms import PostForm
from posts.models import Post


def text_answer(request):
    if request.method == 'GET':
        return HttpResponse('Введение в django, views')


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')


@login_required(login_url='login')
def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'post/post_list.html', context={'posts': posts})


@login_required(login_url='login')
def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'post/post_detail.html', context={'post': post})


@login_required(login_url='login')
def post_create_view(request):

    if request.method == 'GET':
        form = PostForm()
        return render(request, 'post/post_create.html', context={'form': form})

    elif request.method == 'POST':

        # image = request.FILES.get('image')
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # rate = request.POST.get('rate')
        #
        # Post.objects.create(
        #     image=image,
        #     title=title,
        #     content=content,
        #     rate=rate
        # )

        return redirect('/posts/')
