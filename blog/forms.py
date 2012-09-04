from django import forms
from django.forms import ModelForm

class UserBlogPost(ModelForm):
    author = forms.CharField(label=(u'Username'))
    topic = forms.CharField(label=(u'Topic'))
    blogDate = forms.DateTimeField(label=(u'Date'))
    content = forms.Textarea()