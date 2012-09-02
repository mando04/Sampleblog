from django.contrib import admin
from models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'email']}),
        ('Date information', {'fields': ['cDate'], 'classes':['collapse']}),
        (None,               {'fields': ['text']}),
    ]
    list_display = ['name','email','cDate','text']
    search_fields = ['name']

admin.site.register(Post, PostAdmin)
