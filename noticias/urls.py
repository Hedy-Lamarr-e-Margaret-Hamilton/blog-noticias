from django.urls import path
from noticias.views import criar_noticia, painel_noticias

app_name = 'Noticias'
urlpatterns = [
    path('criar_noticia/', criar_noticia, name='criar_noticia'),
    path('painel_noticias/', painel_noticias, name='painel_noticias'),
]