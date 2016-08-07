from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from receitas.models import Receita, Ingrediente, Preparo
from receitas.serializers import ReceitaSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def receitas_list(request):

    if request.method == 'GET':
        receitas = Receita.objects.all()[:10]
        serializer = ReceitaSerializer(receitas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        pass
        # receitas = []
        # entrada = request.POST['ingrediente']
        # ingredientes = []
        #
        # for ing in Ingrediente.objects.filter(nome__contains=entrada):
        #     ingredientes.append(ing)
        #
        # for rec in Receita.objects.filter(ingrediente__in=ingredientes):
        #     receitas.append(rec)
        #
        # serializer = ReceitaSerializer(data=receitas)
        # resposta = {}
        # # import pdb; pdb.set_trace()
        # i = 0
        # serializer.is_valid()
        # for ser in serializer:
        #     if ser.is_valid():
        #         ser.save()
        #         resposta[i] = ser
        #     else:
        #         return JSONResponse(serializer.errors, status=400)
        #
        # return JSONResponse(resposta.data, status=201)


@api_view(['GET'])
@csrf_exempt
def receita_detalhe(request, pk):

    try:
        receita = Receita.objects.get(pk=pk)
    except Receita.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = ReceitaSerializer(receita)
    return Response(serializer.data, status=status.HTTP_200_OK)
