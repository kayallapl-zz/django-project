from rest_framework import serializers

from enderecos.models import Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'data', 'descricao', 'observacoes',]
