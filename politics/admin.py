from django.contrib import admin
from .models import Debate, Comment

admin.site.register(Debate)

class CommentAdmin(admin.ModelAdmin):
    list_display= ('user', 'approved')
    
admin.site.register(Comment, CommentAdmin)
    


