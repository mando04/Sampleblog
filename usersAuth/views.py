from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from usersAuth.forms import RegisterForm, loginUserForm
from usersAuth.models import userAccount
from django.contrib.auth import authenticate, login, logout

def usersRegister(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == ['POST']:
        user = userAccount(bday=request.POST['bday'])
        user.name(request.POST['name'])
        
    else:
        """ user is not submitting a form Show blank form"""
        form = RegisterForm()
        context = {'form': form }
        return render_to_response('register.html', context, context_instance=RequestContext(request))

def loginUser(request):
    form = loginUserForm()
    context = {'form': form }
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                # Redirect to a Success page
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
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    
    return render_to_response('login.html', context, context_instance=RequestContext(request))
 
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
        
            