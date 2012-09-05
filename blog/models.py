from django.db import models
from django.contrib.auth.models import User  
  
class blogPost(models.Model):
    blogDate = models.DateTimeField(auto_now=True, auto_now_add=True)
    topic = models.CharField(max_length=32)
    content = models.TextField()
    author = models.ForeignKey(User, blank=True, null=True)
    