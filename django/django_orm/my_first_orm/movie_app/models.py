from django.db import models

# Create your models here.
# a model will represent a table in our database
class Movie(models.Model):
    # these correspond to the columns in our database
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)