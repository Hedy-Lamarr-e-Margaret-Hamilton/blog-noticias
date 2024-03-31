from django.shortcuts import render
from noticias.forms import NoticiaForm

# Create your views here.
def criar_noticia(request):
    form = NoticiaForm(request.POST or None)
    sucesso = False

    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }
    
    return render(request, 'criar_noticia.html', contexto)