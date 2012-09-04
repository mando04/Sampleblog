from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from blog.models import blogPost
from django.contrib.auth.models import User
from blog.forms import UserBlogFormPost

def index(request):
    post = blogPost.objects.all().order_by('-blogDate')
    stuff = Context({
        'Post': post
    })
    return render_to_response('index.html', stuff, context_instance=RequestContext(request))


def allUserPosts(request, userName):
    authorPost = User.objects.filter(username=userName)
    userPosts = blogPost.objects.filter(author=authorPost)[:]
    return render_to_response('index.html', { 'Post': userPosts }, context_instance=RequestContext(request))

def userBlogPost(request):
    forms = UserBlogFormPost
    stuff = Context({ 'form': forms })
    if request.user.is_authenticated():
        pass
    else:
        error = "You must be <a href='{% url login %}'>logged</a> in to post!"
        stuff.update({'error':error})
        return render_to_response('post.html', stuff, context_instance=RequestContext(request))
    return render_to_response('blog/post.html', stuff, context_instance=RequestContext(request))