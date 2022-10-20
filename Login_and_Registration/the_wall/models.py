from django.db import models
from login.models import User

class Message(models.Model):
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="messages", on_delete = models.DO_NOTHING)

class Comment(models.Model):
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.DO_NOTHING)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.DO_NOTHING)
