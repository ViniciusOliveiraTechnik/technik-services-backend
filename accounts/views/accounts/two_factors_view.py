from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.utils import time_performance
from accounts.services import AccountTwoFactorsService

class AccountTwoFactorsView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    
    @time_performance(detail_name="Validação 2FA do Usuário")
    def post(self, request):
        
        data = request.data
        temporary_auth_token = str(request.auth)
        context = {'request': request, 'request_user': request.user}

        service = AccountTwoFactorsService(context)

        result = service.execute(data, temporary_auth_token)

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