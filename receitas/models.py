from __future__ import unicode_literals

from django.db import models


class Ingrediente(models.Model):
    nome = models.TextField()


class Preparo(models.Model):
    texto = models.TextField()


class Receita(models.Model):
    titulo = models.TextField()
    ingrediente = models.ManyToManyField(Ingrediente, blank=True)
    modo_preparo = models.ManyToManyField(Preparo, blank=True)
