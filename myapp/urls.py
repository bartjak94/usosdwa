from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),  ##edupa cycki zrob tu logowanie i guziczki
	path('lista_studentow',views.students_index, name='students-index'),
	path('usosdwa/<int:book_id>', views.book_detail, name='books-details'),
	path('usosdwa/add', views.book_add, name='books-add')
]