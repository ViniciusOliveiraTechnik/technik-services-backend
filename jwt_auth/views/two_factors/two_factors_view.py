from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from jwt_auth.services.two_factors import TwoFactorsService

class TwoFactorsView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):

        data = request.data 
        temporary_token = str(request.auth)
        context = {'request': request, 'request_user': request.user}

        service = TwoFactorsService(context)

        response_data  = service.execute(data, temporary_token)

        refresh_token = response_data.pop('refresh_token')

        response = Response(response_data)

        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            samesite='Strict',
            secure=True,
        )

        return response