from accounts.services import PasswordResetService
from accounts.permissions import IsOwnerOrAdmin

from jwt_auth.permissions import IsTwoFactorsVerified

from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

class PasswordResetView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsTwoFactorsVerified, IsOwnerOrAdmin]

    def post(self, request, pk):

        data = request.data

        service = PasswordResetService()

        try:

            response_data = service.execute(data, pk)

            return Response(response_data, status=status.HTTP_200_OK)

        except NotFound as err:

            return Response({'error': 'Não foi possível obter o usuário', 'detail': err.detail}, status=status.HTTP_404_NOT_FOUND)
        
        except ValidationError as err:

            return Response({'error': 'Não foi possível validar os dados', 'detail': err.detail}, status=status.HTTP_400_BAD_REQUEST)