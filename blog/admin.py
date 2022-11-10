from django.contrib import admin

from blog.models import Post # agregado para gestionar desde el Admin
from blog.models import Usuario

admin.site.register(Post) # agregado para gestionar desde el Admin
admin.site.register(Usuario)
