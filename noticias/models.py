from django.db import models

# Create your models here.
class Noticia(models.Model):
    categorias = (
        ('Esporte', 'Esporte'),
        ('Cultura', 'Cultura'),
        ('Economia', 'Economia'),
    )

    status = (
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
    )

    titulo = models.CharField(max_length=50)
    autora = models.CharField(max_length=50, default=None)
    data = models.DateField(help_text='dd/mm/aaaa')
    categoria = models.CharField(max_length=50, choices=categorias)
    conteudo = models.TextField()
    destaque = models.BooleanField()
    imagem = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=status)


def __str__(self):
    return f'{self.titulo}: {self.data}'

class Meta:
    verbose_name = 'Cadastro de Notícia'
    verbose_name_plural = 'Cadastro de Notícias'
    ordering = ['-data']