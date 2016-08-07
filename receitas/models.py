from __future__ import unicode_literals

from django.db import models


class Receita(models.Model):
    titulo = models.TextField()
    ingrediente = models.ForeignKey('Ingrediente')
    modo_preparo = models.ForeignKey('Preparo')


class Ingrediente(models.Model):
    nome = models.TextField()


class Preparo(models.Model):
    texto = models.TextField()
