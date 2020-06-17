from django.contrib import admin
from .models import Student, Subject, Login, Error_login, Logout

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Login)
admin.site.register(Error_login)
admin.site.register(Logout)