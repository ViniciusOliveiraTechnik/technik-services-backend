from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound, AuthenticationFailed, ValidationError

from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from accounts.services import PasswordForgotConfirmService
from accounts.utils import time_performance

class PasswordForgotConfirmView(APIView):

    permission_classes = [AllowAny]

    @time_performance
    def post(self, request):
        
        data = request.data
        access_token = str(request.query_params.get('auth'))
        context = {'request': request, 'request_user': request.user}

        service =  PasswordForgotConfirmService(context)

        response_data = service.execute(data, access_token)

        return Response(response_data, status=status.HTTP_200_OK)