from django.db import models
import re

class webManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['firstName']) < 2:
            errors['firstName'] = "First Name must be at least 2 characters!"
        if len(postData['lastName']) < 2:
            errors['lastName'] = "Last Name must be at least 2 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']): # if it doesn't follow the regex email pattern
            errors['email'] = "Invalid Email Address!"
        elif User.objects.filter(email=postData['email']): # returns list, if returns list with item, means the email exists
            errors['emailExists'] = "Account already exists with that email!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        if postData['password'] != postData['confirmPassword']:
            errors['confirmPassword'] = "Passwords do not match, please make sure they match!"
        return errors
    
    def book_validator(self, postData):
        errors = {}
        if not postData['bookTitle']:
            errors['bookTitle'] = "Title is required!"
        if len(postData['bookDesc']) < 5:
            errors['bookDesc'] = "Book Description must be at least 5 characters!"
        return errors

    def edit_validator(self, postData):
        errors = {}
        if not postData['titleToEdit']:
            errors['titleEdit'] = "Title is required!"
        if len(postData['descToEdit']) < 5:
            errors['descEdit'] = "Book Description must be at least 5 characters!"
        return errors

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #books_uploaded (one to many)
    #liked_books (many to many)
    objects = webManager()

class Book(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = webManager()