from django.urls import path
from comentarios.views import criar_coment

app_name = 'comentarios'

urlpatterns = [
    path('criar-coment/', criar_coment),
]