from django.contrib import admin
from noticias.models import Noticia

# Register your models here.
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['data', 'titulo', 'status'] 
    search_field = ['data','titulo']
    list_filter = ['data']