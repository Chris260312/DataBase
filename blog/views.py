from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from .models import Category, Post


def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    context = {
        'categories': categories,
        'posts': posts,
    }

    return render(
        request,
        'index.html',
        context,
    )


def post(request, slug):
    p = Post.objects.filter(
        slug=slug,
    ).first()
    context = {
        'post': p,
    }
    return render(
        request,
        'post.html',
        context,
    )

def get_category(request, slug):
    c = Category.objects.filter(
        slug=slug,
    ).first()
    context = {
        'category': c,
    }
    return render(
        request,
        'category.html',
        context,
    )
# TODO: Доделать функцию вывода
# def get_category(request, slug):
