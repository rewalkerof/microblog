from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


def post_create(request):
    storage = messages.get_messages(request)
    form = PostForm(data=request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Post successfully created!')
        return redirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not successfully created!')
    context = {
        'form': form,
        'messages': storage
    }
    return render(request, 'post_form.html', context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
        'title': 'Detail'
    }
    return render(request, 'post_detail.html', context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
        'title': 'List of posts'
    }
    return render(request, 'post_list.html', context)


def post_edit(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
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
