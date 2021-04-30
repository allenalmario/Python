from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=15)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=15)
    books = models.ManyToManyField(Book, related_name="authors")
    last_name= models.CharField(max_length=15)
    notes = models.TextField(default="Note about author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)