# Generated by Django 4.2.11 on 2024-04-09 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0007_remove_noticia_autora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='sub_titulo',
        ),
    ]