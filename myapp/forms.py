from django import forms
from .models import Student, Subject, Login, Error_login


class LoginForm(forms.ModelForm):
	#password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Login
		fields = '__all__'
		widgets = {'Password': forms.PasswordInput()}

class Error_loginForm(forms.ModelForm):
	class Meta:
		model = Error_login
		fields = '__all__'



class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'


