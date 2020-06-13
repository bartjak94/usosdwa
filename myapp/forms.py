from django import forms
from .models import Student, Subject, Login


class LoginForm(forms.ModelForm):
	class Meta:
		model = Login
		fields = '__all__'

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'
