from django.shortcuts import render

from history.models import Category, Personality


def category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }
    return render(request, 'history/category.html', context)

def personality(request):
    personalities = Personality.objects.filter()
    context = {
        'personalities': personalities,
        'page_title': 'Личности'
    }
    return render(request, 'history/personality.html', context)


def personality_page(request, pk,):
    personality = Personality.objects.get(pk=pk)
    context = {
        'personality': personality,
        'page_title': 'Личность'
    }
    return render(request, 'history/personality_page.html', context)


def index(request):
    return render(request, 'history/index.html')
