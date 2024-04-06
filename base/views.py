from django.shortcuts import render


# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def noticia(request):
    return render(request, 'criar_noticia.html', {})

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