from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from .models import Books
# Create your views here.


def index(request):
    entire_books = Books.objects.all().order_by("-rating")
    return render(request, "books_outlet/books_list.html", {
        "books": entire_books
    })


def book_details(request, slug):
    book = get_list_or_404(Books, slug=slug)[0]
    title = book.title
    brief = book.brief
    author = book.author.all()
    countries = book.published_countries.all()
    rating = book.rating
    is_bestseller = book.is_bestseller
    print(author)
    return render(request, "books_outlet/book_details.html", {
        "title": title,
        "brief": brief,
        "author": author,
        "countries": countries,
        "rating": rating,
        "is_bestseller": is_bestseller
        
    })