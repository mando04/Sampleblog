from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context
from models import Post
import datetime

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        cDate = datetime.datetime.now()
        
        post = Post(name=name)
        post.text = text
        post.cDate = cDate
        
        if name and text and cDate != "":
            post.save()
            return HttpResponseRedirect(reverse('comment.views.index'))
        else:
            error = "All fields are required to post a comment!"
            post = Post.objects.all().order_by(-cDate)[:100]
            return render_to_response('comment/comments.html', { 'Post' : post, 'Error' : error }, context_instance=RequestContext(request))

    post = Post.objects.all().order_by('-cDate')[:5]
    stuff = Context({
        'Post': post
    })
    return render_to_response('comment/comments.html', stuff, context_instance=RequestContext(request))

def allUserComments(request, commentName):
    userComments = Post.objects.filter(name=commentName)
    return render_to_response('comment/comments.html', { 'Post': userComments }, context_instance=RequestContext(request))
