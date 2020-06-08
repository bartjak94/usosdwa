from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Student, Subject
from .models import Book
from .forms import StudentForm
# Create your views here.

def index(request):
	template = loader.get_template("myapp/base.html")
	return render(request, "myapp/base.html")

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
