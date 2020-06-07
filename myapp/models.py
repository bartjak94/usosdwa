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

