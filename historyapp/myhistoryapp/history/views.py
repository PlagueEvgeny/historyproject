from django.shortcuts import render

from history.models import Category


def category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }
    return render(request, 'history/category.html', context)


def index(request):
    return render(request, 'history/index.html')