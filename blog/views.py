from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Context
import datetime,sys,os
from blog.models import blogPost, Author
from usersAuth.models import userAccount
from django.db import IntegrityError

def index(request):
    post = blogPost.objects.all().order_by('-blogDate')
    stuff = Context({
        'Post': post
    })
    return render_to_response('index.html', stuff, context_instance=RequestContext(request))


def allUserPosts(request, userName):
    authorName = Author.objects.filter(fname=userName)
    userPosts = blogPost.objects.filter(author=authorName)
    return render_to_response('index.html', { 'Post': userPosts }, context_instance=RequestContext(request))
