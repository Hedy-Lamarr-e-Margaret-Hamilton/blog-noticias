from typing import Any
from django import forms 
from comentarios.models import Coment
from datetime import date


class ComentForm(forms.ModelForm):
    def clean_data_do_coment(self):
        data = self.cleaned_data['data_do_coment']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Data inválida')
    class Meta:
        model = Coment
        fields = ['nome', 'email', 'text','noticia','data']