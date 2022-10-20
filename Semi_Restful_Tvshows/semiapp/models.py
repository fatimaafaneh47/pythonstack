from django.db import models
import re

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors["title"] = "Blog name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Blog description should be at least 3 characters"
        if len(postData['description']) < 3:
            errors["description"] = "Blog description should be at least 10 characters"
        return errors
      
class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    Realease_Date=models.DateTimeField(auto_now_add=True)
    desc = models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = BlogManager() 



