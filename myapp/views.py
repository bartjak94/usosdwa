from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader


from .models import Book
# Create your views here.

def index(request):
	return HttpResponse("<h1>USOS 2.0 very primitive model</h1>")

def books_index(request):
	template = loader.get_template("myapp/index.html")
	context = {"books": Book.objects.all()}
	return HttpResponse(template.render(context, request))

def book_detail(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	return render(request, "myapp/book.html", {"book":book})

