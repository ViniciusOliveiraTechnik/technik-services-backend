from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
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

        response_data = service.execute(data)

        return Response(response_data, status=status.HTTP_200_OK)
