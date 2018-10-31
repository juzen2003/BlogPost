from django.contrib import admin
# . means the same level of directory
from .models import Post

# Register your models here.
admin.site.register(Post)
