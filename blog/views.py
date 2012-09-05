from django.template import RequestContext, Context
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from blog.models import blogPost
from blog.forms import UserBlogFormPost
import datetime

def index(request):
    post = blogPost.objects.all().order_by('-blogDate')[:]
    stuff = Context({
        'Post': post
    })
    return render_to_response('index.html', stuff, context_instance=RequestContext(request))


def allUserPosts(request, userName):
    authorPost = User.objects.filter(username=userName)
    userPosts = blogPost.objects.filter(author=authorPost)[:]
    return render_to_response('index.html', { 'Post': userPosts }, context_instance=RequestContext(request))

def userBlogPost(request):
    if request.method == 'POST':
        
        topic = request.POST['topic']
        content = request.POST['content']
        dateP = datetime.datetime.now()
        
        post = blogPost(blogDate=dateP)
        post.author = request.user
        post.topic = topic
        post.content = content
        
        if topic and content is not None:
            post.save()
            userPosts = blogPost.objects.all().order_by('-blogDate')[:]
            return render_to_response('index.html', { 'Post': userPosts }, context_instance=RequestContext(request))
        else:
            error = "All fields are required to post!"
            post = blogPost.objects.all().order_by(-dateP)[:100]
            return render_to_response('index.html', \
                                      { 'Post' : post,
                                        'Error' : error }, \
                                       context_instance=RequestContext(request))
        return render_to_response('blog/post.html', {'form':blogPost.objects.all().order_by('-blogDate') }, context_instance=RequestContext(request))
    form = UserBlogFormPost()
    post = blogPost.objects.all().order_by('-blogDate')[:5]
    stuff = Context({
        'Post': post,
        'form': form
    })
    return render_to_response('blog/post.html', stuff, context_instance=RequestContext(request))
        
