from django.db import models
#from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class userAccount(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    bday = models.DateField()
    email = models.EmailField()

    def __unicode__(self):
        return self.name

# create user object
#def createUserCallBack(sender, instance, **kwards):
#    user, new = userAccount.objects.get_or_create(user=instance)
#post_save.connect(createUserCallBack, User)

