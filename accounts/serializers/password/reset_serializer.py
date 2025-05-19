from rest_framework import serializers

class PasswordResetSerializer(serializers.Serializer):

    new_password = serializers.CharField(required=True, write_only=True, min_length=10)
    repeat_new_password = serializers.CharField(required=True, write_only=True, min_length=10)

    def validate(self, attrs):
        
        new_password = attrs.get('new_password')
        repeat_new_password = attrs.get('repeat_new_password')

        if new_password:

            if new_password != repeat_new_password:

                raise serializers.ValidationError('As senhas não coincidem')
            
            return attrs
        
        raise serializers.ValidationError('A senha deve conter pelo menos 10 caracteres')