from django.contrib import admin
from .models import usuario
from .models import mensagem

# Register your models here.

admin.site.register(usuario)
admin.site.register(mensagem)