from django.shortcuts import render, redirect, get_object_or_404
from .models import  * 
from .forms import BookForm, CategoryForm

# Create your views here

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        aad_category = CategoryForm(request.POST)
        if aad_category.is_valid():
            aad_category.save()




    context = {
        'categorys': Category.objects.all(),
        'books': Books.objects.all(),
        'form': BookForm(),
        'form_category': CategoryForm(),
    }

    return render(request, 'pages/index.html', context)

def books(request):
    context = {
        'categorys': Category.objects.all(),
        'books': Books.objects.all(),
    }
    return render(request, 'pages/books.html', context=context )


def update(request, id):
    book_id = Books.objects.get(id=id)
    if request.method == 'POST':
        update_book = BookForm(request.POST, request.FILES, instance=book_id)
        if update_book.is_valid():
            update_book.save()
            return redirect('index')
    else:
        update_book = BookForm(instance=book_id)
    context = {
        'form': update_book,
    }
    return render(request, 'pages/update.html', context=context)


def delete(request, id):
    book_id = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')

