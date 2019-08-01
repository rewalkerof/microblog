from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    storage = messages.get_messages(request)
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Post successfully created!')
        return redirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not successfully created!')
    context = {
        'form': form,
        'title': 'Create post',
        'messages': storage
    }
    return render(request, 'post_form.html', context)


def post_detail(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
        'title': 'Detail'
    }
    return render(request, 'post_detail.html', context)


def post_list(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    list_queryset = Post.objects.all()
    paginator = Paginator(list_queryset, 6)
    page = request.GET.get('page')
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    context = {
        'object_list': lists,
        'title': 'List of posts'
    }
    return render(request, 'post_list.html', context)


def post_edit(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance.save()
        messages.success(request, 'Post successfully edited!')
        return redirect(instance.get_absolute_url())
    else:
        messages.success(request, 'Not successfully edited!')
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form
    }
    return render(request, 'post_form.html', context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.info(request, 'Post succesfully deleted')
    return redirect(instance.get_absolute_url())
