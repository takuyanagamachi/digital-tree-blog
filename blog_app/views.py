# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostAddForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

#お問い合わせ
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail

def is_valid_q(q):
    return q != '' and q is not None

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    title_or_user = request.GET.get('title_or_user')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    tag = request.GET.get('tag')

    if is_valid_q(title_or_user):
        posts = posts.filter(Q(title__icontains=title_or_user)
                       | Q(user__username__icontains=title_or_user)
                       ).distinct()

    if is_valid_q(date_min):
        posts = posts.filter(created_at__gte=date_min)

    if is_valid_q(date_max):
        posts = posts.filter(created_at__lt=date_max)

    if is_valid_q(tag) and tag != 'タグを選択...':
        posts = posts.filter(tag__tag=tag)
    
    return render(request, 'blog_app/index.html', 
    {'posts': posts, 'title_or_user': title_or_user , 'date_min': date_min, 'date_max': date_max ,'tag': tag})


def detail(request, post_id):
      post = get_object_or_404(Post, id=post_id)
      return render(request, 'blog_app/detail.html', {'post': post})

@login_required
def add(request):
    if request.method == "POST":
       form = PostAddForm(request.POST, request.FILES)
       if form.is_valid():
          post = form.save(commit=False)
          post.user = request.user
          post.save()
          return redirect('blog_app:index')
    else:   
        form = PostAddForm()
    return render(request, 'blog_app/add.html', {'form': form})

@login_required
def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_app:detail', post_id=post.id)
    else:
        form = PostAddForm(instance=post)
    return render(request, 'blog_app/edit.html', {'form': form, 'post':post })

@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('blog_app:index')


#お問い合わせ
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           subject = form.cleaned_data['subject']
           message = form.cleaned_data['message']
           sender = form.cleaned_data['sender']
           myself = form.cleaned_data['myself']
           recipients = [settings.EMAIL_HOST_USER]
           if myself:
                recipients.append(sender)
           try:
                send_mail(subject, message, sender, recipients)
           except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
           return redirect('blog_app:done')
    else:
        form = ContactForm()
    return render(request, 'blog_app/contact.html', {'form': form})

def done(request):
    return render(request, 'blog_app/done.html')