from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def pesquisa(request):
    return render(request, 'pesquisa.html', {})

def detalhes_noticia(request, id):
    return HttpResponse(f"Detalhes da notícia com ID {id}")

def noticias_por_categoria(request, categoria):
    return HttpResponse(f"Notícias da categoria {categoria}")

def autores(request):
    return HttpResponse("Lista de autores de notícias")

def noticias_por_autor(request, id):
    return HttpResponse(f"Notícias do autor com ID {id}")