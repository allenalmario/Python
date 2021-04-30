from django.db import models

# Create your models here.
class FormManager(models.Manager):
    def add_validator(self, request):
        errors = {}
        if len(request["showTitle"]) < 2:
            errors["showName"] = "Show name should be at least 2 characters"
        if len(request["showNetwork"]) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(request["showDesc"]) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors
    
    def edit_validator(self, request):
        errors = {}
        if len(request["titleToEdit"]) < 2:
            errors["title"] = "Show name should be at least 2 characters"
        if len(request["networkToEdit"]) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(request["descToChange"]) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=30)
    network = models.CharField(max_length=30)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FormManager()