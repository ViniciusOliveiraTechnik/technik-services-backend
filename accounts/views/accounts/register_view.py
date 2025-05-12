from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from accounts.utils import time_performance
from accounts.services import AccountRegisterService

class AccountRegisterView(APIView):
    """
    View to handle user registration.
    """
    permission_classes = [AllowAny]
    
    @time_performance(detail_name="Registro de Usuário")
    def post(self, request):
        """
        Handle POST request to register a new user.

        Args:
            request: The HTTP request containing user data.
        
        Returns:
            Response: A response indicating success or failure of the registration.
        """
        try:

            data = request.data
            context = {'request': request}

            service = AccountRegisterService(context)

            response_data = service.execute(data)

            return Response({'message': 'Usuário criado com sucesso!', 'user': response_data}, status=status.HTTP_201_CREATED)
        
        except ValidationError as err:

            return Response({'error': 'Não foi possível criar o usuário', 'detail': err.detail})