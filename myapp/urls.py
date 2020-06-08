from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='main-menu'),  ##edupa cycki zrob tu logowanie i guziczki
	path('lista_studentow',views.students_index, name='students-index'),
	#path('usosdwa/<int:book_id>', views.book_detail, name='books-details'),
	path('add', views.student_add, name='student-add')
]