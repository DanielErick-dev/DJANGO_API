from rest_framework import serializers
from .models import ApiAluno
from django.shortcuts import get_object_or_404
class ModelSerializerApi(serializers.ModelSerializer):
    class Meta:
        model = ApiAluno
        fields = ['id', 'name', 'lastname', 'cpf', 'created_at', 'expiration_date', 'phone_number' ]

    def validate_cpf(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("O campo CPF não pode conter letras")
        if len(value) != 11:
            raise serializers.ValidationError("O campo CPF deve ter 11 dígitos")
        if ApiAluno.objects.filter(cpf=value).exists():
            raise serializers.ValidationError("esse CPF já está cadastrado no sistema, insira outro")
        return value
    def validate_phone_number(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("número de telefone inválido")
        if value[2] != '9':
            raise serializers.ValidationError("número adicional de telefone inválido")
        if ApiAluno.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("esse número de telefone já está cadastrado no sistema, insira outro")
        if not value.isdigit():
            raise serializers.ValidationError("campo de telefone deve conter apenas números sem espaços ou traços")
        return value
    
    def validate_lastname(self, value):
        if value == 'teste':
            raise serializers.ValidationError("O campo sobrenome não pode ser 'teste'")
        if value == '':
            raise serializers.ValidationError("O campo sobrenome não pode ser vazio")
        return value

    def validate_name(self, value):
        if value == 'teste':
            raise serializers.ValidationError("O campo nome não pode ser 'teste")
        if value == '':
            raise serializers.ValidationError("O campo nome não pode ser vazio")
        
        return value
    def validate(self, data):
        print(f'validando dados: {data}')
        if data['name'] == data['lastname']:
            print('nomes são iguais')
            raise serializers.ValidationError("o campo nome não pode ser igual ao campo sobrenome")
        
        return data