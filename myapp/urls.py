from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('lista_studentow',views.students_index, name='students-index'),
	path('add', views.student_add, name='student-add'),
	path('student/<int:student_id>', views.student_details),
	path('subjects_index',views.subjects_index, name='subjects-index'),
	path('subject_add', views.subject_add, name='subject-add'),
<<<<<<< HEAD
	path('after_login', views.after_login_view, name='after_loginName'),
	path('error_login', views.error_login_view, name='error_loginName'),
	path('logout',  auth_views.LogoutView.as_view(), name='logoutName'),
	path('subject/<int:subject_id>', views.subject_details),
	path('login/', views.user_login, name='login')
=======
	path('subject/<int:subject_id>', views.subject_details),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout')
>>>>>>> logowanietest

]