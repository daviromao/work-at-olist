from pyexpat import model
from tabnanny import verbose
from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=255, unique=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Book(models.Model):
	name = models.CharField(max_length=255)
	edition = models.PositiveSmallIntegerField(default=1)
	publication_year = models.PositiveSmallIntegerField()
	authors = models.ManyToManyField(Author, related_name="books")

	class Meta:
		ordering = ['-publication_year']
	
	def __str__(self):
		return self.name