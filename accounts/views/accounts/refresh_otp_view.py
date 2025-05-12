from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, NotAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.permissions import IsOwnerOrAdmin
from accounts.services import AccountRefreshOtpService

class AccountRefreshOtpView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def post(self, request, pk):

        service = AccountRefreshOtpService()

        try:

            response_data = service.execute(pk)

            return Response(response_data, status=status.HTTP_200_OK)
        
        except NotAuthenticated as err:

            return Response({'error': 'O usuário não está autenticado para utilizar esse serviço', 'detail': err.detail}, status=status.HTTP_401_UNAUTHORIZED)
        
        except NotFound as err:

            return Response({'error': 'Usuário não existente', 'detail': err.detail}, status=status.HTTP_404_NOT_FOUND)