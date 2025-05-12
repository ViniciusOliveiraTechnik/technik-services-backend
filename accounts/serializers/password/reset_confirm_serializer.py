from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password

class PasswordResetConfirmSerializer(serializers.Serializer):

    password = serializers.CharField(write_only=True)

    def validate_password(self, value):

        validate_password(value)

        return value
    