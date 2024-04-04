from django.contrib import admin
from comentarios.models import Comentario


# Register your models here.

@admin.register(Comentario)
class ComentAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email','texto','noticia', 'data']
    list_filter = ['data']
    search_fields = ['noticia', 'nome']
    