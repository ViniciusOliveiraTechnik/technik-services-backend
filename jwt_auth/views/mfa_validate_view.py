from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from jwt_auth.services.auth import AuthMFAValidateService
from jwt_auth.authentications import MFAJWTAuthentication

class AuthMFAValidateView(APIView):

    authentication_classes = [MFAJWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):

        access_token = str(request.auth)
        data = request.data 
        context = {'request': request, 'request_user': request.user}

        service = AuthMFAValidateService(context)

        result  = service.execute(access_token, data)

        refresh_token = result.pop('refresh_token')

        response = Response(result)

        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            samesite='Strict',
            secure=True,
        )

        return response