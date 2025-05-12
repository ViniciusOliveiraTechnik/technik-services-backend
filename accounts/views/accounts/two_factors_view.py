from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.exceptions import InvalidToken

from accounts.utils import time_performance
from accounts.services import AccountTwoFactorsService


class AccountTwoFactorsView(APIView):

    permission_classes = [AllowAny]
    
    @time_performance(detail_name="Validação 2FA do Usuário")
    def post(self, request):
        
        try:

            data = request.data
            auth = str(request.auth)
            context = {'request': request}

            service = AccountTwoFactorsService(context)

            response_data = service.execute(data, auth)

            return Response(response_data, status=status.HTTP_200_OK)
        
        except ValidationError as err:

            return Response({'error': 'O código de autenticação está incorreto ou expirou. Tente novamente.', 'detail': err.detail}, status=status.HTTP_400_BAD_REQUEST)
        
        except NotFound as err:

            return Response({'error': 'Usuário não encontrado', 'detail': err.detail}, status=status.HTTP_404_NOT_FOUND)

        except InvalidToken as err:

            return Response({'error': 'Token inválido ou expirado', 'detail': err.detail}, status=status.HTTP_401_UNAUTHORIZED)