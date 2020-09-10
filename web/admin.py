from django.contrib import admin
from .models import Mail, Post

admin.site.register(Post)
admin.site.register(Mail)