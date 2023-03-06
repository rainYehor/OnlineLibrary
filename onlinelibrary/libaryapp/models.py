from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)