from django import forms
from django.forms import ModelForm
from models import blogPost

class UserBlogFormPost(ModelForm):
    author = forms.CharField(label=(u'Username'))
    topic = forms.CharField(label=(u'Topic'))
    blogDate = forms.DateTimeField(label=(u'Date'))
    content = forms.Textarea()

    class Meta:
        model = blogPost