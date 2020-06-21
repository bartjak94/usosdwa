from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Student, Subject, Login, Error_login
from .models import Book
from .forms import StudentForm, SubjectForm, LoginForm, Error_loginForm
# Create your views here.


@login_required
def dashboard(request):
	return render(request,'myapp/dashboard.html', {'section': 'dashboard'})
@login_required
def index(request):
	template = loader.get_template("myapp/base.html")
	return render(request, "myapp/base.html")

@login_required
def students_index(request):
	template = loader.get_template("myapp/index.html")
	context = {"students": Student.objects.all()}
	return HttpResponse(template.render(context, request))

@login_required
def student_add(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('students-index'))
	else:
		form = StudentForm()
		return render(request, "myapp/student_add.html", {'form': form})

@login_required
def student_details(request, student_id):
	student = Student.objects.get(pk=student_id)
	return render(request, "myapp/student_details.html", {"student": student})

@login_required
def subjects_index(request):
    template = loader.get_template("myapp/subjects_index.html")
    context = {"subjects":Subject.objects.all()}
    return HttpResponse(template.render(context, request))

@login_required
def subject_add(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('subjects-index'))
    else:
        form = SubjectForm()
        return render(request, "myapp/subject_add.html", {'form': form})

@login_required
def subject_details(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    return render(request, "myapp/subject_details.html", {"subject": subject})

