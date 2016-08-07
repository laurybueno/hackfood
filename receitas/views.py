from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from receitas.models import Receita, Ingrediente, Preparo
from receitas.serializers import ReceitaSerializer


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def receitas_list(request):

    if request.method == 'GET':
        receitas = Receita.objects.all()
        serializer = ReceitaSerializer(receitas, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        pass
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JSONResponse(serializer.data, status=201)
        # return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def receita_detalhe(request, pk):

    try:
        receita = Receita.objects.get(pk=pk)
    except Receita.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReceitaSerializer(receita)
        return JSONResponse(serializer.data)
