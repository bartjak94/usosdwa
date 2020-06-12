from django.db import models

# Create your models here.

class Author(models.Model):
	first_name = models.CharField(max_length=50)
	surname = models.CharField(max_length=100)

	def __str__(self):
		return "{} {}".format(self.surname, self.first_name)


class Book(models.Model):
	title = models.CharField(max_length=200)
	pages = models.IntegerField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	decription = models.TextField(default='')

	def __str__(self):
		return "{}".format(self.title)



class Student(models.Model):
	numer_id = models.IntegerField()
	first_name = models.CharField(max_length=50)
	surname = models.CharField(max_length=100)
	semester = models.IntegerField()
	specjalizejszyn = models.CharField(max_length=10)
	def __str__(self):
		return "{} {} {} {} {}".format(self.numer_id, self.first_name, self.surname, self.semester, self.specjalizejszyn)


class Subject(models.Model):
	sub_id = models.IntegerField()
	sub_name = models.CharField(max_length=50)
	students = models.ManyToManyField(Student)
	def __str__(self):
		return "{} {} {}".format(self.sub_id, self.sub_name, self.students)
        
        
class Login(models.Model):
	log_id = models.IntegerField()
	log_name = models.CharField(max_length=50)
	def __str__(self):
		return "{} {} {}".format(self.log_id, self.sub_name)