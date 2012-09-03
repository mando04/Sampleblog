from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from usersAuth.forms import RegisterForm

def index(request):
   return HttpResponseRedirect('/')
 
def usersRegister(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == ['POST']:
        pass
    else:
        """ user is not submitting a form Show blank form"""
        form = RegisterForm()
        context = {'form': form }
        return render_to_response('register.html', context, context_instance=RequestContext(request))

