from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from secrets import token_hex

from .helpers import getAnioPlayTimeGenre

@api_view(['GET'])
def PlayTimeGenre(request, genero: str):
    anio = getAnioPlayTimeGenre(genero)
    data = {"Anio de lanzamiento con mas horas jugadas para Genero {}".format(genero) : anio}
    return JsonResponse(data, status=status.HTTP_200_OK)
    # Si se ingresa un genero que no existe:
    #return JsonResponse({"message": "genero no existe"}, status=status.HTTP_404_NOT_FOUND)
