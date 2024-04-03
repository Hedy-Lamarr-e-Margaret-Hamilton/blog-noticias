from django.db import models 

# Create your models here.
class Comentario(models.Model):
    
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    text = models.TextField()
    noticia = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    
    
class Meta:
    verbose_name = 'Cadastro de comentario'
    verbose_name_plural = 'Cadastros de comentarios'
    ordering = ['data']

   