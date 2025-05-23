from rest_framework import serializers

class AccountTwoFactorsSerializer(serializers.Serializer):

    otp_code = serializers.CharField(required=True)

    def validate_otp_code(self, value):
        
        if len(value) > 6:

            raise serializers.ValidationError('O código de autenticação deve conter apenas 6 digitos')
        
        return value