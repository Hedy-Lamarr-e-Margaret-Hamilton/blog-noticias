from django import forms 
from comentarios.models import Coment

class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ['nome', 'email', 'text','noticia','data']