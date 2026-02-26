from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from .models import Books
from django.views.generic import View, ListView, DetailView
# Create your views here.


class IndexView(ListView):
    model = Books
    template_name = "books_outlet/books_list.html"
    context_object_name = "books"
    ordering = "-rating"



class BookDetailsView(DetailView):
    model = Books
    template_name = "books_outlet/book_details.html"
    context_object_name = "book"
    slug_field = "slug"
    slug_url_kwarg = "slug"