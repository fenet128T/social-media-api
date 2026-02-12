from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Post
from .models import Follow

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Post)
admin.site.register(Follow)
