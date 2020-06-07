from django.db import models

# Create your models here.
<<<<<<< HEAD
class Author(models.Model):
	first_name = models.CharField(max_length=50)
	surname = models.CharField(max_length=100)

	def __str__(self):
		return "{} {}".format(self.surname, self.first_name)


class Book(models.Model):
	title = models.CharField(max_length=200)
	pages = models.IntegerField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.title)
=======
>>>>>>> e6458622cfa2b0d08475818c9aa468dc17d3494a
