from rest_framework import serializers

class PasswordForgotRequestSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)