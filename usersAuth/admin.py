from django.contrib import admin
from usersAuth.models import userAccount

class userAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['user', 'name', 'email']}),
        ('Date information', {'fields': ['bday']}),
            ]
    list_display = ['name','email','user']
    search_fields = ['user']
    
admin.site.register(userAccount, userAdmin)

