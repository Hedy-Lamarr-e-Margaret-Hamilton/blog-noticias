from django.shortcuts import render

from noticias.models import Noticia


# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def noticia(request):
    return render(request, 'criar_noticia.html', {})

def pesquisar_noticias_por_categoria(request, categoria):
    noticias = Noticia.objects.filter(categoria=categoria)
    return render(request, 'pesquisar_noticias.html', {'noticias': noticias, 'categoria': categoria})

def noticia_por_categoria(request, categoria=None):
    noticias = Noticia.objects.all()  # Retorna todas as notícias por padrão
    
    if categoria:
        noticias = noticias.filter(categoria=categoria)

    categorias = {
        'tecnologia': {'imagem': '/static/images/tecnologia.jpg', 'nome': 'Tecnologia'},
        'economia': {'imagem': '/static/images/economia.jpg', 'nome': 'Economia'},
        'cultura': {'imagem': '/static/images/cultura.jpg', 'nome': 'Cultura'},
        'politica': {'imagem': '/static/images/politica.jpg', 'nome': 'Política'},
        'esportes': {'imagem': '/static/images/esportes.jpg', 'nome': 'Esportes'}
    }

    return render(request, 'noticia_por_categoria.html', {'noticias': noticias, 'categoria': categoria, 'categoria_info': categorias.get(categoria)})

def noticia_por_id(request, id):
    # Busca a notícia pelo ID no banco de dados
    noticia = Noticia.objects.get(pk=id)
    return render(request, 'noticia_por_id.html', {'noticia': noticia})

def comentario(request):
    return render(request, 'comentario.html')

def tecnologia(request):
    return render(request, 'tecnologia.html')

def politica(request):
    return render(request, 'politica.html')

def economia(request):
    return render(request, 'economia.html')

def esportes(request):
    return render(request, 'esportes.html')

def cultura(request):
    return render(request, 'cultura.html') 