from rest_framework import serializers
from receitas.models import Receita, Ingrediente, Preparo


class ReceitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receita
        fields = ('titulo', 'ingrediente', 'modo_preparo')
        depth = 1
