from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from usersAuth.models import userAccount

class RegisterForm(ModelForm):
    username = forms.CharField(label=(u'User Name'))
    bday = forms.DateField(label=(u'Birhday'))
    email = forms.EmailField(label=(u'Emaill address'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
 

    class Meta:
        model = userAccount
        exclude = ('user', userAccount)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, please try again")

    def clean_password(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise forms.ValidationError("The Passwords didn't match, please try again")
        return password

class loginUserForm(forms.Form):
    username = forms.CharField(label=(u'Username'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    