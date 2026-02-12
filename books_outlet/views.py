from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *
# Create your views here.


def index(request):

    return render(request, "books_outlet/books_list.html")