from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=25)
    text = models.TextField()
    cDate = models.DateTimeField()
    email = models.EmailField(blank=True)