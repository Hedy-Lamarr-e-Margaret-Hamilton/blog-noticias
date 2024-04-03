from django.db import models 

# Create your models here.
class Comentario(models.Model):
    
    
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    noticia = models.TextField()
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.noticia}:{self.nome}, {self.texto}'
class Meta:
    verbose_name = 'Cadastro de comentario'
    verbose_name_plural = 'Cadastros de comentarios'
    ordering = ['data']

   