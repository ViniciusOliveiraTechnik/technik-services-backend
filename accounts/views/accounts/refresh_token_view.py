from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from accounts.services import AccountRefreshTokenService
from accounts.utils import time_performance

class AccountRefreshTokenView(APIView):

    permission_classes = [AllowAny]

    @time_performance(detail_name='Obter novo Access Token')
    def post(self, request):

        refresh_token = str(request.COOKIES.get('refresh_token'))
        context = {'request': request, 'request_user': request.user}

        service = AccountRefreshTokenService(context)

        response_data = service.execute(refresh_token)

        return Response(response_data, status=status.HTTP_200_OK)