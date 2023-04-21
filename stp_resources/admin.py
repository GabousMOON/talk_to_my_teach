from django.contrib import admin
from .models import Post, WebResource, Question

# Register your models here.
admin.site.register(Post)
admin.site.register(WebResource)
admin.site.register(Question)
from .models import Post
