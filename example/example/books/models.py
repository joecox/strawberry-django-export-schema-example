from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)


class Series(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)