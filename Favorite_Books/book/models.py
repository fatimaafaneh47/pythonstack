from django.db import models
from login.models import User
import re 

class BookManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}
        if len(post_data['title'])<1:
            errors['title']='title is required'
        if len(post_data['description'])<5:
            errors['description']='must be more than 5 charectors'
        return errors


class Book(models.Model):
    Title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name="books")
    user = models.ForeignKey(User, related_name="book_user", on_delete = models.DO_NOTHING)
    objects = BookManager() 
