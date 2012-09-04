from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from usersAuth.forms import RegisterForm, loginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from usersAuth.models import userAccount

def usersRegister(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], \
                                            email=form.cleaned_data['email'], \
                                            password=form.cleaned_data['password'])
            user.save()
            
            USER_P = userAccount(user=user, name=form.cleaned_data['name'], \
                                 bday=form.cleaned_data['bday'], \
                                 email=form.cleaned_data['email'])
            USER_P.save()
            
            return HttpResponseRedirect('/loggedin')
        else:
            return render_to_response('register.html', { 'form':form }, context_instance=RequestContext(request))    
    else:
        """ user is not submitting a form Show blank form"""
        form = RegisterForm()
        context = {'form': form }
        return render_to_response('register.html', context, context_instance=RequestContext(request))

def loginUser(request):
    context = {'form': loginUserForm }

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    
    if request.method == 'POST':
        form = loginUserForm(request.POST)
        if form.is_valid():
            user = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=user, \
                                password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    error = "Account is diabled please email the Site Administrator"
                    #return a 'disabled account' error message
                    context.update({'error':error})
                    return render_to_response('login.html', context, context_instance=RequestContext(request))
            else:
                error = "Username or password was incorrect!"
                context.update({'error':error})
                # return an 'invalid login' error page
                return render_to_response('login.html', context, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', { 'form':form }, context_instance=RequestContext(request))

    return render_to_response('login.html', context, context_instance=RequestContext(request))

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
