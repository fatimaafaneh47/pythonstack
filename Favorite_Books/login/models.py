from distutils.log import error
from typing import Text
from django.db import models
import re 
from django.core.validators import validate_email

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}
        if len(post_data['first_name'])<1:
            errors['first_name']='please enter youre first name'
        if len(post_data['last_name'])<1:
            errors['last_name']='please enter youre last name'
        try: 
             validate_email(post_data['email'])
        except:
             errors['email']='please enter a valid email'
        if len(post_data['password'])<1:
            errors['password']='please enter a password'
        if post_data['password'] !=post_data['confirm_pw']:
            errors['confirm_pw'] ='youre password didnt match'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password = models.CharField(max_length=60)
    confirm_pw = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager() 






