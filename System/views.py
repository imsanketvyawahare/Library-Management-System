from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Library


def home(request):
    books = Library.objects.all()
    return render(request, 'home.html', {"books": books})


def add(request):
    if request.method == 'POST':
        book = Library()
        book.book_id = request.POST['book-id']
        book.book_name= request.POST['book-name']
        book.book_author = request.POST['book-author']
        book.date_of_publish = request.POST['date']
        book.book_price = request.POST['book-price']
        book.save()
        return redirect('home')
    else:
        return render(request, 'add.html')


def delete(request, id):
    book = Library.objects.get(book_id=id)
    book.delete()
    return redirect('home')


def update(request, id):
    if request.method == 'POST':
        book = Library.objects.get(book_id=id)
        book.book_id = request.POST['book-id']
        book.book_name = request.POST['book-name']
        book.book_author = request.POST['book-author']
        book.date_of_publish = request.POST['date']
        book.book_price = request.POST['book-price']
        book.save()
        return redirect('home')
    else:
        book = Library.objects.get(book_id=id)
        date = str(book.date_of_publish)
        return render(request, 'update.html', {"books": book, "date":date})
