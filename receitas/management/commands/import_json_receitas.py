# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from receitas.models import Receita, Ingrediente, Preparo

import json
from pprint import pprint


class Command(BaseCommand):
    args = 'file'
    help = 'Importar um json de receitas no banco de dados'

    def limpeza(texto):
        return texto.replace('\n', '')

    @transaction.atomic
    def handle(self, *args, **options):
        count = 0
        with open(args[0]) as arq:

            ingredientes = []
            modo_preparo = []

            for obj in json.load(arq):
                # Itera a lista de ingredientes
                for ing in obj['ingredientes'].values():
                    ingredientes.append(Ingrediente.objects.get_or_create(
                        nome=ing
                    )[0])

                # Itera a lista de instruções de Preparo
                for prep in obj['modo_preparo'].values():
                    modo_preparo.append(Preparo.objects.get_or_create(
                        texto=prep
                    )[0])

                titulo = obj['titulo']

                rec = Receita.objects.create(
                    titulo=titulo
                )

                # Associa dados à receita atual
                for mod in modo_preparo:
                    rec.modo_preparo.add(mod)

                for ing in ingredientes:
                    rec.ingrediente.add(ing)

                # Salva a receita
                rec.save()

                count += 1
                print(count)
