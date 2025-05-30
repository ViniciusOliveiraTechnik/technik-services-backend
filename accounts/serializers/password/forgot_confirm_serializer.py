from rest_framework import serializers

class PasswordForgotConfirmSerializer(serializers.Serializer):

    password = serializers.CharField(required=True, write_only=True)
    same_password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):

        password = str(attrs.get('password')).strip()
        
        same_password = str(attrs.get('same_password')).strip()

        if password != same_password:

            raise serializers.ValidationError('As senhas devem coincidir')
        
        attrs['password'] = password

        attrs['same_password'] = same_password

        return attrs
