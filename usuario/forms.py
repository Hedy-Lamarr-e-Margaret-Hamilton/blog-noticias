
from django import forms
from usuario.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'email', 'senha', 'role']