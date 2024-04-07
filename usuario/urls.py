from django.urls import path
from usuario.views import criar_user, login

app_name = "usuario"
urlpatterns = [
    path('criar/', criar_user),
    path('login/', login),
]
