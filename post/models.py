from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Blog(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
       content = models.TextField(default='hi')
       created_at = models.DateTimeField(auto_now_add=True,null=True)
       updated_at = models.DateTimeField(auto_now=True,null=True)
       

       def __str__(self):
        return self.content[:20]
    
