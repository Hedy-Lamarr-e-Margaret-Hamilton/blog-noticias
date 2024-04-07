from django.shortcuts import render, redirect
from usuario.models import User
from usuario.forms import UserForm, UserLoginForm

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

def login(request):
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        if User.objects.filter(email=form.cleaned_data['email'], senha=form.cleaned_data['senha']).exists():
            return redirect('noticias:criar_noticia')
        else:
            form.add_error(None, 'Usuário não encontrado.')
    
    return render(request, 'login.html', { 'form': form })
