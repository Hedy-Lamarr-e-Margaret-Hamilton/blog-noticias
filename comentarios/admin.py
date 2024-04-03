from django.contrib import admin
from comentarios.models import Coment


# Register your models here.

@admin.register(Coment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email','texto', 'noticia','data']
    list_filter = ['data']
    search_fields = ['nome']
    