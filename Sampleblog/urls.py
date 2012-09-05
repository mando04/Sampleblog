from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.index', name='home'),
    url(r'^login/$', 'usersAuth.views.loginUser', name='login'),
    url(r'^blog/post/$', 'blog.views.userBlogPost', name='post'),
    url(r'^logout/$', 'usersAuth.views.logoutUser', name='logout'),
    url(r'^register/$', 'usersAuth.views.usersRegister', name='register'),
    url(r'^posts/(?P<userName>[-\w]+)/all/$', 'blog.views.allUserPosts'),
    url(r'^comment/allcomments/(?P<commentName>[-\w]+)/all/$', 'comment.views.allUserComments'),
    url(r'^comment/delete/(?P<comment_id>\d+)$', 'comment.views.deletepost'),
    url(r'^comment/comments.html$', 'comment.views.index', name='comment'),
    
    #display static content
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : STATIC_ROOT}),
    # url(r'^$', 'Sampleblog.views.home', name='home'),
    # url(r'^Sampleblog/', include('Sampleblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
