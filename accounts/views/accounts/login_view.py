from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from accounts.utils import time_performance
from accounts.services import AccountLoginService

class AccountLoginView(APIView):

    permission_classes = [AllowAny]

    @time_performance(detail_name='Login de Usuário')
    def post(self, request):

        data = request.data
        context = {'request': request, 'request_user': request.user}
    
        service = AccountLoginService(context)

        result = service.execute(data)

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

