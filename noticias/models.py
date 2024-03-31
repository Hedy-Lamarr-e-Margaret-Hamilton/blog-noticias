from django.db import models

# Create your models here.
class Noticia(models.Model):
    categorias = (
        ('Esporte', 'Esporte'),
        ('Cultura', 'Cultura'),
        ('Economia', 'Economia'),
    )

    categoria = models.CharField(max_length=50, choices=categorias)
    conteudo = models.TextField()
    data = models.DateField(help_text='dd/mm/aaaa')
    destaque = models.BooleanField()
    imagem = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    titulo = models.TextField()

def __str__(self):
    return f'{self.titulo}: {self.data}'

class Meta:
    verbose_name = 'Cadastro de Notícia'
    verbose_name_plural = 'Cadastro de Notícias'
    ordering = ['-data']