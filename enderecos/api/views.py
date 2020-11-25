from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from enderecos.models import Endereco
from enderecos.api.serializers import EnderecoSerializer


@api_view(['GET', ])
def api_detail_enderecos(request, id):
    try:
        endereco = Endereco.objects.get(id=id)
    except Endereco.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)
