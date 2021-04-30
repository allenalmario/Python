from django.db import models
import re
import bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class webManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters"
        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid email address!"
        elif User.objects.filter(email=postData['email']):
            errors['exist'] = "Email is unavailable!"
        if len(postData['password']) < 8:
            errors['lengthPassword'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['passwordMatch'] = "Passwords do not match, please make sure you type the passwords correctly"
        return errors

    def login_validator(self, postData):
        errors = {}
        if not email_regex.match(postData['loginEmail']):
            errors['invalidLoginEmail'] = "Not a valid Email address!"
        if not postData['loginEmail']:
            errors['loginEmailError'] = "Login Email required!"
        if not postData['loginPassword']:
            errors['loginPasswordError'] = "Login Password required!"
        return errors

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #many messages
    #many comments
    objects = webManager()

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #many comments

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)