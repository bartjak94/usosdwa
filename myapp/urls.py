from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('books',views.books_index, name='books-index'),
	path('books/<int:book_id>', views.book_detail, name='books-details'),
]