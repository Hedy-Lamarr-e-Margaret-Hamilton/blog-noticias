from django.shortcuts import render
from usuario.models import User
from usuario.forms import UserForm

# Create your views here.
def criar_user(request):
    sucesso = False
    form = UserForm(request.POST or None)
    
    if form.is_valid():
        sucesso = True
        form.save()
        
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }
    
    return render(request, 'criar_usuario.html', contexto)
