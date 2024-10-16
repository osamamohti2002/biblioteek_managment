from django.shortcuts import render
from .models import  * 

# Create your views here

def index(request):
    context = {
        'books': Books.objects.all(),
    }

    return render(request, 'pages/index.html', context)

def books(request):
    return render(request, 'pages/books.html')

def delete(request):
    return render(request, 'pages/delete.html')

def update(request):
    return render(request, 'pages/update.html')