from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from posts.forms import PostForm, SearchForm, PostUpdateForm
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
        search = request.GET.get('search')
        tags = request.GET.getlist('tags')
        orderings = request.GET.get('orderings')
        searchform = SearchForm(request.GET)
        page = int(request.GET.get('page', 1))
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if tags:
            posts = posts.filter(tags__id__in=tags)
        if orderings:
            posts = posts.order_by(orderings)

        limit = 4
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)
        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]

        context = {'posts': posts, 'search_form': searchform, 'max_pages': range(1, max_pages+1)}
        return render(request, 'post/post_list.html', context=context)


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
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'post/post_create.html', context={'form': form})
        form.save()
        return redirect('/posts/')


@login_required(login_url='login')
def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = PostUpdateForm(instance=post)
        return render(request, 'post/post_update.html', context={'form': form})
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, 'post/post_update.html', context={'form': form})
        form.save()
        return redirect('/posts/')
