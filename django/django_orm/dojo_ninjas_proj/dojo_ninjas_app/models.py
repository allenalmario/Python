from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    desc = models.TextField(default="Old Dojo")

class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
