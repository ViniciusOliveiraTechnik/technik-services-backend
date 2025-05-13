from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound, AuthenticationFailed, ValidationError

from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from accounts.services import PasswordForgotService
from accounts.utils import time_performance

class PasswordForgotConfirmView(APIView):

    permission_classes = [AllowAny]

    @time_performance
    def post(self, request):
        
        data = request.data
        tokem_param = request.query_params.get('token')

        service = PasswordForgotService()

        try:

            response_data = service.execute_confirm(data, tokem_param)

            return Response(response_data, status=status.HTTP_200_OK)
        
        except ValidationError as err:

            return Response({'error': 'Credenciais passadas são inválidas', 'detail': err.detail}, status=status.HTTP_400_BAD_REQUEST)
        
        except AuthenticationFailed as err:

            return Response({'error': 'Não foi possível localizar o token de acesso', 'detail': err.detail}, status=status.HTTP_401_UNAUTHORIZED)
        
        except TokenError as err:

            return Response({'error': 'Ação do token não compatível', 'detail': err.detail}, status=status.HTTP_401_UNAUTHORIZED)

        except InvalidToken as err:

            return Response({'error': 'O token de acesso expirou ou é inválido. Tente novamente', 'detail': err.detail}, status=status.HTTP_401_UNAUTHORIZED)
        
        except NotFound as err:

            return Response({'error': 'Usuário não encontrado', 'detail': err.detail}, status=status.HTTP_404_NOT_FOUND)