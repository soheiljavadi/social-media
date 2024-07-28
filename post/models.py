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
       pic = models.ImageField('Image',
                            upload_to='Post_image',
                            help_text='picture for post',)
       

       def __str__(self):
        return self.content[:20]
       
class Like(models.Model):
     Blog = models.ForeignKey(Blog, related_name='likes', on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
        
class Comment(models.Model):
    Blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(default='hello')
   
    def __str__(self):
        return  {self.user.first_name} 



     
