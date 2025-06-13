from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from jwt_auth.services.auth import AuthMFASetupService
from jwt_auth.authentications import MFAJWTAuthentication

class AuthMFASetupView(APIView):

    authentication_classes = [MFAJWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):

        access_token = str(request.auth)
        data = request.data
        context = {'request': request, 'request_user': request.user}

        service = AuthMFASetupService(context)

        result = service.execute(access_token, data)

        refresh_token = result.pop('refresh_token')

        response = Response(result)

        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            samesite='Strict',
            secure=True
        )

        return response