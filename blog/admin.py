from django.contrib import admin
from models import Author, blogPost

class PostAdmin(admin.ModelAdmin):
    search_fields = ['topic']
    list_display = ['topic']
    
admin.site.register(blogPost, PostAdmin)

admin.site.register(Author)
