from django.db import models

# Create your models here.
class Author(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    aEmail = models.EmailField(blank=True)

    def __unicode__(self):
        return u"%s %s - %s" % (self.fname, self.lname, self.aEmail)
    
class blogPost(models.Model):
    blogDate = models.DateTimeField(auto_now=True, auto_now_add=True)
    topic = models.CharField(max_length=32)
    content = models.TextField()
    author = models.ForeignKey(Author)
    
