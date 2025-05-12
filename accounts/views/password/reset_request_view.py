from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError

from accounts.services import PasswordResetService
from accounts.utils import time_performance

class PasswordResetRequestView(APIView):

    permission_classes = [AllowAny]

    @time_performance
    def post(self, request):

        data = request.data

        service = PasswordResetService()

        try:

            response_data = service.execute_request(data)

            return Response(response_data, status=status.HTTP_200_OK)

        except ValidationError as err:

            return Response({'error': 'Os dados enviados são inválidos', 'detail': err.detail}, status=status.HTTP_400_BAD_REQUEST)