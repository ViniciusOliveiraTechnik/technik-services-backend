from django.contrib.auth import authenticate

from rest_framework import serializers

class AccountLoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):

        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:

            raise serializers.ValidationError("Email ou senha inválidos")

        user = authenticate(username=email, password=password)

        if not user:

            raise serializers.ValidationError('As credenciais estão incorretas')
        
        if not user.is_active:

            raise serializers.ValidationError('O usuário não está ativo')
        
        data['user'] = user

        return data