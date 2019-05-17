
from django.contrib import admin
from .models import Image, Tag, Profile, Comment

# Register your models here.
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Profile)