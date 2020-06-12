from django import forms
from .models import Student, Subject


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'
