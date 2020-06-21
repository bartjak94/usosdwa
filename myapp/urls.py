from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('menu', views.index, name='main-menu'),  ##edu
	path('', views.dashboard, name='dashboard'),  ##edu
	path('lista_studentow',views.students_index, name='students-index'),
	path('add', views.student_add, name='student-add'),
	path('student/<int:student_id>', views.student_details),
	path('subjects_index',views.subjects_index, name='subjects-index'),
	path('subject_add', views.subject_add, name='subject-add'),
    #path('log_in', views.log_in2, name='login'),
	path('after_login', views.after_login_view, name='after_loginName'),
	path('error_login', views.error_login_view, name='error_loginName'),
	#path('logout', views.logout_view, name='logoutName'),
	path('subject/<int:subject_id>', views.subject_details),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout')

]