from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from receitas.models import Receita, Ingrediente, Preparo
from receitas.serializers import ReceitaSerializer


@csrf_exempt
@api_view(['GET'])
def receitas_list(request):

    if request.method == 'GET':
        receitas = Receita.objects.all()[:10]
        serializer = ReceitaSerializer(receitas, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
def receitas_busca(request, ingredientes):

    ingredientes = []

    for ing in Ingrediente.objects.filter(nome__contains=ingredientes):
        ingredientes.append(ing)

    receitas = []
    for rec in Receita.objects.filter(ingrediente__in=ingredientes):
        receitas.append(rec)

    serializer = ReceitaSerializer(receitas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
def receita_detalhe(request, pk):

    try:
        receita = Receita.objects.get(pk=pk)
    except Receita.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = ReceitaSerializer(receita)
    return Response(serializer.data, status=status.HTTP_200_OK)
