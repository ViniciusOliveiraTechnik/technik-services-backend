from rest_framework import serializers

class AuthOtpSerializer(serializers.Serializer):

    otp_code = serializers.CharField(required=True, write_only=True)

    def validate_otp(self, value):

        length = len(value)

        if not isinstance(value, str):

            raise serializers.ValidationError('O código de autenticação deve ser do tipo texto')

        if 6 > length > 6:

            raise serializers.ValidationError('O código de autenticação deve conter 6 digitos')
        
        return value