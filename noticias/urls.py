from django.urls import path
from noticias.views import criar_noticia

app_name = 'Noticias'
urlpatterns = [
    path('criar_noticia/', criar_noticia, name='criar_noticia'),
]