from django.contrib import admin
from .models import Post, WebResource, Question, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(WebResource)
admin.site.register(Question)
from .models import Post, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')