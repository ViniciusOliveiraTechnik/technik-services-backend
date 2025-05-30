from rest_framework import serializers

class PasswordForgotSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)