from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post,Gallery


admin.site.register(Post)
admin.site.register(Gallery)