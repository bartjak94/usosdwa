from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Student, Subject, Login, Error_login
from .models import Book
from .forms import StudentForm
from .forms import SubjectForm
from .forms import LoginForm
from .forms import Error_loginForm
# Create your views here.

def index(request):
	template = loader.get_template("myapp/base.html")
	return render(request, "myapp/base.html")


def error_login_view(request):
	template = loader.get_template("myapp/error_login.html")
	return render(request, "myapp/error_login.html")


def students_index(request):
	template = loader.get_template("myapp/index.html")
	context = {"students": Student.objects.all()}
	return HttpResponse(template.render(context, request))


def student_add(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('students-index'))
	else:
		form = StudentForm()
		return render(request, "myapp/student_add.html", {'form': form})

def student_details(request, student_id):
	student = Student.objects.get(pk=student_id)
	return render(request, "myapp/student_details.html", {"student": student})

def subjects_index(request):
    template = loader.get_template("myapp/subjects_index.html")
    context = {"subjects":Subject.objects.all()}
    return HttpResponse(template.render(context, request))

def subject_add(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('subjects-index'))
    else:
        form = SubjectForm()
        return render(request, "myapp/subject_add.html", {'form': form})

def subject_details(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    return render(request, "myapp/subject_details.html", {"subject": subject})

def log_in(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('main-menu'))
	else:
		form = LoginForm()
		return render(request, "myapp/log_in.html", {'form': form})

def log_in2(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if(form.is_valid()):
			form.save()
			#return HttpResponseRedirect(reverse('main-menu'))
			return render(request, "myapp/after_login.html", {'form': form})
		else:
			return render(request, "myapp/error_login.html", {'form': form})
			#return HttpResponseRedirect(reverse('main-menu'))

	else:
		form = LoginForm()
		return render(request, "myapp/log_in.html", {'form': form})


def after_login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('after_loginName'))
		else:
			#return render(request, "myapp/error_login.html", {'form': form})
			#return HttpResponseRedirect(reverse('error_loginName'))
			return render(request, "myapp/after_login.html", {'form': form})

	else:
		form = LoginForm()
		return render(request, "myapp/error_login.html", {'form': form})