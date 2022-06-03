from django.shortcuts import render
from .models import *

# Create your views here.

def category(request):
    categories = Category.objects.all()
    return render(request, 'drink.html', {'categories': categories})

def detail(request, name):
    category = Category.objects.get(name=name)
    drinks = Drink.objects.filter(category=category)
    return render(request, 'detail.html', {'drinks': drinks})

