from django import forms
from noticias.models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['categoria', 'conteudo', 'data', 'destaque', 'imagem', 'status', 'titulo']