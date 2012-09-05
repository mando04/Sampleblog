from django.contrib import admin
from blog.models import blogPost
from usersAuth.models import userAccount

class PostAdmin(admin.ModelAdmin):
    search_fields = ['topic']
    list_display = ['topic']
    
admin.site.register(blogPost, PostAdmin)