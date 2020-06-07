from django.shortcuts import render
from django.http import HttpResponse

from .models import Book
# Create your views here.

def index(request):
	return HttpResponse("<h1>USOS 2.0 very primitive model</h1>")

def books_index(request):
	books = [book.title + " " + "<b>" + book.author.surname + "</b>" for book in Book.objects.all()]
	wyjscie = "</br>".join(books)
	return HttpResponse(wyjscie)