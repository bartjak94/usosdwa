from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='main-menu'),  ##edupa cycki zrob tu logowanie i guziczki
	path('lista_studentow',views.students_index, name='students-index'),
	path('add', views.student_add, name='student-add'),
	path('student/<int:student_id>', views.student_details),
	path('subjects_index',views.subjects_index, name='subjects-index'),
	path('subject_add', views.subject_add, name='subject-add'),
<<<<<<< HEAD
    path('logg', views.log_in, name='login'),
=======
	path('logg', views.log_in, name='login'),
>>>>>>> 8607864f655ca4ddbad1e3cedf246ee5b8c89ce6
	path('subject/<int:subject_id>', views.subject_details)

    #testing git functionality
]