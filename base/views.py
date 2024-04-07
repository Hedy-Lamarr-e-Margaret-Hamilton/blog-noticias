from django.shortcuts import render, redirect
from noticias.models import Noticia

def inicio(request):
    #noticias_urgentes
    #ultimas_noticias (puxar as mais recentes)
    return render(request, 'index.html')

def pesquisar_noticias(request):
    pesquisa_formulario = request.POST.get('search_query')
    if pesquisa_formulario:
        noticias = Noticia.objects.filter(conteudo__icontains=pesquisa_formulario)
        return render(request, 'pesquisar_noticias.html', {'noticias': noticias, 'pesquisa_formulario': pesquisa_formulario})
    else:
        return render(request, 'pesquisa_nao_encontrada.html', {'pesquisa_formulario': pesquisa_formulario})

def pesquisa_nao_encontrada(request):
    return render(request, 'pesquisa_nao_encontrada.html')

def noticia(request):
    return render(request, 'criar_noticia.html', {})

def pesquisar_noticias_por_categoria(request, categoria):
    # Pesquisar notícias com base na categoria
    noticias = Noticia.objects.filter(categoria=categoria)
    return render(request, 'pesquisar_noticias.html', {'noticias': noticias})

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