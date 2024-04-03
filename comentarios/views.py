from django.shortcuts import render
from comentarios.forms import ComentForm
from django.views.decorators.cache import cache_page
from comentarios.models import Comentario

# Create your views here.
@cache_page(30)
def criar_coment(request):
    comentarios = Comentario.objects.all()
    sucesso = False
    form = ComentForm(request.POST or None)

    if form.is_valid():
        form.save()
        sucesso = True

    contexto = {
        'form': form,
        'sucesso': sucesso,
        'comentarios': comentarios,
    }

    return render(request, 'criar_coment.html', contexto)